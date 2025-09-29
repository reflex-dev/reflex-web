import os
import typesense
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TYPESENSE_CONFIG = {
    'nodes': [{
        'host': os.getenv('TYPESENSE_HOST'),
        'port': '443',
        'protocol': 'https'
    }],
    'api_key': os.getenv('TYPESENSE_ADMIN_API_KEY'),
    'connection_timeout_seconds': 60
}

# Conversation history collection schema
CONVERSATION_SCHEMA = {
    'name': 'conversations',
    'fields': [
        {'name': 'id', 'type': 'string'},
        {'name': 'conversation_id', 'type': 'string', 'facet': True},
        {'name': 'model_id', 'type': 'string', 'facet': True},
        {'name': 'role', 'type': 'string', 'facet': True},  # 'user' or 'assistant'
        {'name': 'message', 'type': 'string'},
        {'name': 'timestamp', 'type': 'int32'},
    ]
}

class ConversationSetup:
    def __init__(self):
        self.client = typesense.Client(TYPESENSE_CONFIG)

    def create_conversation_collection(self, force_recreate: bool = False):
        """Create the conversation history collection"""
        try:
            # Check if collection exists
            try:
                self.client.collections['conversations'].retrieve()
                if force_recreate:
                    logger.info("Deleting existing conversation collection...")
                    self.client.collections['conversations'].delete()
                else:
                    logger.info("Conversation collection already exists. Use force_recreate=True to recreate.")
                    return True
            except typesense.exceptions.ObjectNotFound:
                pass

            logger.info("Creating conversation collection...")
            self.client.collections.create(CONVERSATION_SCHEMA)
            logger.info("Conversation collection created successfully.")
            return True

        except Exception as e:
            logger.error(f"Error creating conversation collection: {e}")
            return False


    def setup_all(self, force_recreate: bool = False):
        """Setup conversation collection and test RAG configuration"""
        success = True

        if not self.create_conversation_collection(force_recreate):
            success = False

        return success


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Setup Typesense Conversational RAG')
    parser.add_argument('--force', action='store_true', help='Force recreate collections and models')
    args = parser.parse_args()

    # Validate environment variables
    required_vars = ['TYPESENSE_HOST', 'TYPESENSE_ADMIN_API_KEY', 'GEMINI_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        logger.error(f"Missing required environment variables: {missing_vars}")
        return False

    setup = ConversationSetup()
    success = setup.setup_all(force_recreate=args.force)

    if success:
        logger.info("Conversational RAG setup completed successfully!")
    else:
        logger.error("Setup failed. Check the logs above for details.")

    return success

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
