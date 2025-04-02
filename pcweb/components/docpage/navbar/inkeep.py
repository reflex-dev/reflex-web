"""UI and logic inkeep chat component."""

from typing import List, Any

import reflex as rx
from reflex.event import EventHandler
from reflex.utils.imports import ImportVar
from reflex.vars import Var


class InkeepSearchBar(rx.NoSSRComponent):
    tag = "InkeepSearchBar"
    library = "@inkeep/cxkit-react@0.5.9"


class Search(rx.el.Div):
    def add_imports(self):
        """Add the imports for the component."""
        return {
            "react": {ImportVar(tag="useContext")},
            "$/utils/context": {ImportVar(tag="ColorModeContext")},
        }

    def add_hooks(self):
        """Add the hooks for the component."""
        return [
            "const { resolvedColorMode } = useContext(ColorModeContext)",
            """
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
      // Add inline styles using the recommended approach from the docs
      styles: [
        {
          key: "custom-theme",
          type: "style",
          value: `
            [data-theme='light'] .ikp-search-bar__button,
            [data-theme='dark'] .ikp-search-bar__button {
              display: flex;
              max-height: 32px;
              min-height: 32px;
              padding: 6px;
              min-width: 256px;
              justify-content: space-between;
              align-items: center;
              border-radius: 10px;
              border: 1px solid var(--c-slate-5, #E0E1E6);
              background: var(--c-slate-1);
              /* Small */
              font-family: "Instrument Sans";
              font-size: 14px;
              font-style: normal;
              font-weight: 500;
              line-height: 20px;
              /* 142.857% */
              letter-spacing: -0.0125em;
              color: var(--c-slate-9, #8B8D98);
              /* Shadow/Large */
              box-shadow: 0px 24px 12px 0px rgba(28, 32, 36, 0.02), 0px 8px 8px 0px rgba(28, 32, 36, 0.02), 0px 2px 6px 0px rgba(28, 32, 36, 0.02);
              transition: background-color 0.1s linear, width 0s;
            }
            
            [data-theme='light'] .ikp-search-bar__button:hover,
            [data-theme='dark'] .ikp-search-bar__button:hover {
              background-color: var(--c-slate-3, #F0F0F3);
            }
            
            [data-theme='dark'] .ikp-modal__overlay {
              background: rgba(18, 17, 19, 0.50);
              backdrop-filter: blur(20px);
            }
            
            @media (max-width: 80em) {
              [data-theme='light'] .ikp-search-bar__button,
              [data-theme='dark'] .ikp-search-bar__button {
                padding: 2px 12px;
                display: block;
                height: 32px;
                min-height: 32px;
                width: 32px;
                max-width: 6em;
                min-width: 0px;
              }
            
              .ikp-search-bar__button {
                align-items: center;
                justify-content: center;
              }
            
              .ikp-search-bar__kbd-wrapper,
              .ikp-search-bar__text {
                display: none;
              }
            
              .ikp-search-bar__icon {
                padding: 0;
                margin-right: 2px;
              }
            
              .ikp-search-bar__content-wrapper {
                justify-content: center;
              }
            }
            
            .ikp-search-bar__icon {
              display: flex;
            }
            
            .ikp-search-bar__icon svg {
              width: auto;
            }
            
            .ikp-search-bar__kbd-wrapper {
              padding: 0px 8px;
              justify-content: center;
              align-items: center;
              border-radius: 4px;
              box-shadow: none;
              color: var(--c-slate-9, #8B8D98);
              font-family: "Instrument Sans";
              --ikp-colors-transparent: var(--c-slate-3, #FCFCFD);
              background: var(--c-slate-3, #F0F0F3) !important;
              font-size: 12px;
              font-style: normal;
              font-weight: 500;
              line-height: 20px;
              /* 166.667% */
              letter-spacing: -0.09px;
            }
            
            .ikp-search-bar__text,
            .ikp-search-bar__icon {
              color: var(--c-slate-9, #8B8D98);
              font-weight: 500;
            }
          `,
        },
        {
          key: "google-fonts-instrument",
          type: "link",
          value: "https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;700&display=swap",
        },
      ],
      components: {
        SearchBarTrigger: {
          defaultProps: {
            variant: 'subtle', // 'emphasized' 'subtle'
            size: 'expand',
          },
        },
      },
      // Add this to ensure CSS variables are applied
      varsClassName: "ikp-variables",
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

    @classmethod
    def create(cls):
        """Create the search component."""
        return super().create(
            InkeepSearchBar.create(
                special_props=[Var("{...searchBarProps}")],
            )
        )


inkeep = Search.create
