import os
import time
import uuid
from typing import List, Dict, Any
import typesense
import reflex as rx


TYPESENSE_CONFIG = {
    "nodes": [{"host": os.getenv("TYPESENSE_HOST"), "port": "443", "protocol": "https"}],
    "api_key": os.getenv("TYPESENSE_SEARCH_API_KEY"),
    "connection_timeout_seconds": 10,
}



class Message(rx.Base):
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: float
    message_id: str = ""
    sources: List[Dict[str, Any]] = []

class ConversationalSearch(rx.State):
    # Chat state
    current_message: str = ""
    messages: List[Message] = []
    conversation_id: str = ""
    is_loading: bool = False
    error_message: str = ""

    @rx.event(temporal=True)
    def update_current_message(self, message: str):
        self.current_message = message

    @rx.event(temporal=True)
    def clear_error(self):
        self.error_message = ""

    @rx.event(temporal=True)
    def start_new_conversation(self):
        """Start a new conversation"""
        self.conversation_id = ""  # Reset to empty - let Typesense generate new one
        self.messages = []
        self.current_message = ""
        self.error_message = ""
        print("Started new conversation")


    def _get_snippet(self, document: Dict, highlights: List[Dict]) -> str:
        """Extract snippet from highlights or content"""
        if highlights:
            for highlight in highlights:
                if highlight.get("field") in ["content", "title"]:
                    snippets = highlight.get("snippets", [])
                    if snippets:
                        return snippets[0]

        # Fallback to document content
        content = document.get("content", "")
        return content[:200] + "..." if len(content) > 200 else content

    def _extract_key_terms(self, query: str) -> str:
        """Extract key technical terms from conversational queries for better search"""
        import re

        # Common question words and filler words to remove
        stop_words = {
            # Existing core
            'how', 'do', 'i', 'can', 'you', 'what', 'is', 'are', 'the', 'in', 'to',
            'use', 'with', 'for', 'a', 'an', 'and', 'or', 'but', 'of', 'on', 'at',
            'by', 'this', 'that', 'it', 'from', 'they', 'be', 'been', 'have', 'has',
            'had', 'will', 'would', 'could', 'should', 'may', 'might', 'must',
            'does', 'did', 'was', 'were', 'am', 'about', 'help', 'me', 'please',
            'get', 'make', 'create', 'build', 'add', 'set', 'up', 'work', 'works', 'reflex',
            'tell',

            # Additional common stopwords
            'as', 'if', 'then', 'than', 'so', 'because', 'also', 'just', 'now', 'only',
            'really', 'very', 'even', 'still', 'some', 'any', 'more', 'most', 'much',
            'into', 'out', 'over', 'under', 'again', 'there', 'here', 'when', 'where',
            'why', 'who', 'whom', 'whose', 'which', 'while', 'too',

            # Pronouns and variations
            'my', 'mine', 'your', 'yours', 'he', 'him', 'his', 'she', 'her', 'hers',
            'we', 'us', 'our', 'ours', 'their', 'them', 'theirs', 'itself', 'yourself',
            'ourselves', 'themselves',

            # Contractions and negations
            "i'm", "i've", "i'd", "i'll",
            "you're", "you've", "you'd", "you'll",
            "he's", "he'd", "he'll",
            "she's", "she'd", "she'll",
            "it's", "it'd", "it'll",
            "we're", "we've", "we'd", "we'll",
            "they're", "they've", "they'd", "they'll",
            "isn't", "aren't", "wasn't", "weren't",
            "hasn't", "haven't", "hadn't",
            "doesn't", "don't", "didn't",
            "won't", "wouldn't", "can't", "couldn't", "shouldn't", "mustn't", "shan't",

            # Fillers and common noise
            "ok", "okay", "yeah", "yes", "no", "uh", "um", "like",

            # Contextual terms (image-related, generative)
            "image", "photo", "picture", "draw", "drawing", "show", "generate", "render", "display"
        }


        # Important technical terms that should always be kept
        important_terms = {
            'reflex', 'tailwind', 'css', 'state', 'component', 'event', 'handler',
            'style', 'styling', 'layout', 'frontend', 'backend', 'api', 'database',
            'auth', 'authentication', 'routing', 'deploy', 'deployment', 'config',
            'installation', 'setup', 'props', 'variables', 'functions', 'class',
            'import', 'export', 'javascript', 'python', 'html', 'reactjs', 'nextjs',
            'dynamic', 'routes', 'wrap', 'react', 'components'
        }

        # Clean and tokenize
        # Remove punctuation except hyphens and underscores
        cleaned = re.sub(r'[^\w\s-]', ' ', query.lower())
        words = re.findall(r'\b\w+\b', cleaned)

        # Filter words
        key_terms = []
        for word in words:
            # Keep if it's an important technical term
            # if word in important_terms:
            #     key_terms.append(word)
            # Keep if it's not a stop word and longer than 2 chars
            if word not in stop_words and len(word) > 2:
                key_terms.append(word)

        # Remove duplicates while preserving order
        seen = set()
        unique_terms = []
        for term in key_terms:
            if term not in seen:
                seen.add(term)
                unique_terms.append(term)

        # If we have key terms, use them; otherwise fall back to original
        if unique_terms:
            result = ' '.join(unique_terms)
            return result

        # Fallback: just remove common question starters
        fallback = re.sub(r'^(how do i|how to|what is|can i|how can i)\s+', '', query.lower())
        return fallback.strip() or query

    @rx.event(background=True, temporal=True)
    async def send_message(self):
        """Send a message and get AI response using Typesense conversational search"""
        if not self.current_message.strip():
            return

        # Add user message
        user_message = Message(
            role="user",
            content=self.current_message.strip(),
            timestamp=time.time(),
            message_id=str(uuid.uuid4())
        )

        async with self:
            self.messages.append(user_message)
            self.is_loading = True
            self.error_message = ""
            original_query = self.current_message
            self.current_message = ""
            yield

        try:
            client = typesense.Client(TYPESENSE_CONFIG)

            # Extract key terms from the conversational query for better search
            search_query = self._extract_key_terms(original_query)
            print(f"Original query: {original_query}")
            print(f"Search query: {search_query}")

            # Search parameters matching your working search, with conversation enabled
            # BUT: Don't use conversation_id - treat each question independently
            search_params = {
                "q": original_query,  # Use processed query for search
                "query_by": "title,content,headings,components",
                "query_by_weights": "6,8,3,12",
                "per_page": 15,
                "num_typos": 2,
                "sort_by": "_text_match:desc",
                "text_match_threshold": "0.6",
                "exhaustive_search": True,
                "highlight_fields": "content",
                "highlight_full_fields": "content,components",
                "highlight_start_tag": "<mark>",
                "highlight_end_tag": "</mark>",
                "snippet_threshold": 30,
                "filter_by": "url:!~blog",  # Exclude blogs
                "conversation": "true",
                "conversation_model_id": "reflex-docs-convo",
                "exclude_fields": "hits.document.content"  # <-- this is the key change
            }

            # result = client.collections["docs"].documents.search(search_params)

            result = client.collections["docs"].documents.search({
                "q": search_query,
                "query_by": "title,content",
                "num_typos": 2,
                "conversation": True,
                "conversation_model_id": "reflex-docs-convo",
                "exclude_fields": "hits.document.content"
            })

            # # Debug what we found
            # if result.get("hits"):
            #     top_hit = result["hits"][0]
            #     doc = top_hit["document"]
            #     print(f"Top hit: {doc.get('title')} at {doc.get('url')}")
            # else:
            #     print("No hits found!")

            # Extract the conversation response
            conversation = result.get("conversation", {})
            ai_response = conversation.get("answer", "")

            print(f"AI Response: {ai_response}")

            if not ai_response:
                ai_response = "I couldn't generate a response. Please try rephrasing your question."

            print("Final AI Answer Only:", ai_response)

            # Create assistant message with only the AI answer
            assistant_message = Message(
                role="assistant",
                content=ai_response,
                timestamp=time.time(),
                message_id=str(uuid.uuid4()),
                sources=[]  # Empty sources for clean answer-only response
            )

            async with self:
                self.messages.append(assistant_message)
                self.is_loading = False
                yield

        except Exception as e:
            print(f"Error in send_message: {str(e)}")
            import traceback
            traceback.print_exc()

            async with self:
                self.messages.append(Message(
                    role="assistant",
                    content=f"I encountered an error: {str(e)}. Please try again.",
                    timestamp=time.time(),
                    message_id=str(uuid.uuid4())
                ))
                self.is_loading = False
                self.error_message = f"Error: {str(e)}"
                yield

    @rx.event(temporal=True)
    def retry_last_message(self):
        """Retry the last user message if there was an error"""
        if self.messages and self.messages[-1].role == "user":
            self.current_message = self.messages[-1].content
            # Remove the last message and any error response
            if len(self.messages) > 1 and "error" in self.messages[-1].content.lower():
                self.messages = self.messages[:-1]
