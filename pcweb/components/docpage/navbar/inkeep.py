"""UI and logic inkeep chat component."""

from typing import List, Set

import reflex as rx
from reflex.event import EventHandler
from reflex.utils.imports import ImportVar
from reflex.vars import Var


class Search(rx.Component):
    tag = "SearchBar"

    special_props: List[Var] = [Var("{...searchBarProps}")]

    is_open: Var[bool] = False

    on_close: EventHandler[lambda: []]

    on_shortcut_key_pressed: EventHandler[lambda: []]

    class_name: Var[str] = "max-w-[256px] max-h-[32px]"

    def add_imports(self):
        """Add the imports for the component."""
        return {
            "next/dynamic": {ImportVar(tag="dynamic", is_default=True)},
            "react": {ImportVar(tag="useContext")},
            "$/utils/context": {ImportVar(tag="ColorModeContext")},
        }

    def add_hooks(self):
        """Add the hooks for the component."""
        return [
            "const { resolvedColorMode } = useContext(ColorModeContext)",
            """const SearchBar = dynamic(
  () => import('@inkeep/uikit').then((mod) => mod.InkeepSearchBar),
  {
    ssr: false,
  },
);
const supportFormConfig = {
  heading: "Contact support",
  fields: [
    {
      type: "STANDARD_FIELD",
      label: "Name",
      name: "first_name",
      inputType: "TEXT",
    },
    {
      type: "STANDARD_FIELD",
      label: "Company Email",
      name: "email",
      inputType: "EMAIL",
      required: true,
    },
    {
      type: "INCLUDE_CHAT_SESSION",
      defaultValue: true,
    },
    {
      type: "STANDARD_FIELD",
      label: "Additional details",
      name: "additional_details",
      inputType: "TEXTAREA",
    },
    {
      type: 'STANDARD_FIELD',
      label: 'Category',
      name: 'category',
      inputType: 'SELECT',
      selectOptions: [
        { label: 'Bug', value: 'BUG' },
        { label: 'Feature idea', value: 'FEATURE' },
        { label: 'Account access', value: 'ACCOUNT' },
      ],
    },
  ],
  submitCallback: async (values) => {
    const discordWebhookUrl = "https://discord.com/api/webhooks/1313281051765903372/5w4g9xxKa5naY5I6I9esNxeT5rI66t75MniNNPFM7bBoagQuDZamgqQdoHIFqYh6x_7J";
    if (!discordWebhookUrl) {
      console.error("Discord webhook URL is not set in the environment.");
      return;
    }
    
    const { formDetails, chatSession, client } = values;

    // Build the chat history string manually
    let chatHistory = "**Chat History:**";
    const messages = chatSession?.messages || [];
    for (let i = 0; i < messages.length; i++) {
      const msg = messages[i];
      const role = msg.role === "user" ? "User" : "Assistant";
      chatHistory += ` **${i + 1}. ${role}:** ${msg.content}\n`;
    }

    // Build a simple and readable message
    const discordMessage = `
  **New Support Request**

  **Name:** ${formDetails.first_name || "N/A"}
  **Email:** ${formDetails.email || "N/A"}
  **Category:** ${formDetails.category || "N/A"}
  **Additional Details:** ${formDetails.additional_details || "N/A"}

  **Current Page URL:** ${client?.currentUrl || "N/A"}

  **Chat Session ID:** ${chatSession?.chatSessionId || "N/A"}
  ${chatHistory || "**Chat History:** No messages available."}
  `;

    // Prepare the payload
    const payload = { content: discordMessage };

    try {
      // Send the payload to the Discord webhook
      const response = await fetch(discordWebhookUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`Failed to send message: ${response.statusText}`);
      }

      console.log("Values sent successfully to Discord!");
    } catch (error) {
      console.error("Error sending values to Discord:", error);
    }
    return { success: true };
  },
};
const searchBarProps = {
  stylesheetUrls: ['/inkeepstyle-docs.css'],
  baseSettings: {
    apiKey: '87b7469f79014c35a3313795088151a52de8a58a547abd16',
    integrationId: 'clkbf9e7e0001s601sa0ciax1',
    customIcons: {search: {custom: "/icons/search.svg"}},
    organizationId: 'org_WQKeNdnuPGEfuUhC',
    organizationDisplayName: 'Reflex',
    primaryBrandColor: '#6E56CF',
    consoleDebugLevel: 1,
    breadcrumbRules: {
      urlToBreadcrumbMapper: [
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/blog',
          },
          breadcrumbName: 'Blogs',
        },
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs',
          },
          breadcrumbName: 'Docs',
        },
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs/api-reference',
          },
          replaceLeading: true,
          breadcrumbName: 'API Reference',
        },
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs/library',
          },
          replaceLeading: true,
          breadcrumbName: 'Components',
        },
      ],
    },
    colorMode: {
      forcedColorMode: resolvedColorMode, // options: 'light' or dark'
    },
    theme: {
      stylesheetUrls: ['/inkeepstyle-docs.css'],
      components: {
        SearchBarTrigger: {
          defaultProps: {
            variant: 'subtle', // 'emphasized' 'subtle'
            size: 'expand',
          },
        },
      },
    }
  },
  searchSettings: { // optional InkeepSearchSettings
    tabSettings: {
      isAllTabEnabled: true,
      useAllRootBreadcrumbsAsTabs: true,
      rootBreadcrumbsToUseAsTabs: ['All', 'Docs', 'Components', 'API Reference', 'Blogs'],
      tabOrderByLabel: ['All', 'Docs', 'Components', 'API Reference', 'Blogs'],
    },
    placeholder: 'Search',
  },
  aiChatSettings: { // optional typeof InkeepAIChatSettings
    quickQuestions: [
      'How does Reflex work?',
      'What types of apps can I build with Reflex?',
      'Where can I deploy my apps?',
    ],
    includeAIAnnotations: {
      shouldEscalateToSupport: true,
    },
    aiAnnotationPolicies: {
      shouldEscalateToSupport: [
        {
          threshold: "STANDARD", // "STRICT" or "STANDARD"
          action: {
            type: "SHOW_SUPPORT_BUTTON",
            label: "Contact Support",
            action: {
              type: "OPEN_FORM",
              formConfig: supportFormConfig,
            },
          },
        },
      ],
    },
    getHelpCallToActions: [
      {
        name: 'Get help',
        type: 'OPEN_FORM',
        formConfig: supportFormConfig,
      },
    ],
  },
};""",
        ]


inkeep = Search.create
