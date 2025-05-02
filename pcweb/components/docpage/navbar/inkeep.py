"""UI and logic inkeep chat component."""

import reflex as rx
from reflex.utils.imports import ImportVar
from reflex.vars import Var


class InkeepSearchBar(rx.NoSSRComponent):
    tag = "InkeepSearchBar"
    library = "@inkeep/cxkit-react@0.5.55"


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
const escalationParams = {
  type: "object",
  properties: {
    explanation: {
      type: "string",
      description: "A brief few word justification of why a specific confidence level was chosen.",
    },
    answerConfidence: {
      anyOf: [
        {
          type: "string",
          const: "very_confident",
          description: `\n    The AI Assistant provided a complete and direct answer to all parts of the User Question.\n    The answer fully resolved the issue without requiring any further action from the User.\n    Every part of the answer was cited from the information sources.\n    The assistant did not ask for more information or provide options requiring User action.\n    This is the highest Answer Confidence level and should be used sparingly.\n  `,
        },
        {
          type: "string",
          const: "somewhat_confident",
          description: `\n    The AI Assistant provided a complete and direct answer to the User Question, but the answer contained minor caveats or uncertainties. \n \n    Examples:\n    • The AI Assistant asked follow-up questions to the User\n    • The AI Assistant requested additional information from the User\n    • The AI Assistant suggested uncertainty in the answer\n    • The AI Assistant answered the question but mentioned potential exceptions\n  `,
        },
        {
          type: "string",
          const: "not_confident",
          description: `\n    The AI Assistant tried to answer the User Question but did not fully resolve it.\n    The assistant provided options requiring further action from the User, asked for more information, showed uncertainty,\n    suggested the user contact support or provided contact information, or provided an indirect or incomplete answer.\n    This is the most common Answer Confidence level.\n \n    Examples:\n    • The AI Assistant provided a general answer not directly related to the User Question\n    • The AI Assistant said to reach out to support or provided an email address or contact information\n    • The AI Assistant provided options that require further action from the User to resolve the issue\n  `,
        },
        {
          type: "string",
          const: "no_sources",
          description: `\n    The AI Assistant did not use or cite any sources from the information sources to answer the User Question.\n  `,
        },
        {
          type: "string",
          const: "other",
          description: `\n    The User Question is unclear or unrelated to the subject matter.\n  `,
        },
      ],
      description: "A measure of how confidently the AI Assistant completely and directly answered the User Question.",
    },
  },
  required: ["explanation", "answerConfidence"],
  additionalProperties: false,
};
const searchBarProps = {
  baseSettings: {
    apiKey: '6299820854cd95d0a6e55a502d5bae06549e62360e7805a6',
    customIcons: {search: {custom: "/icons/search.svg"}},
    organizationDisplayName: 'Reflex',
    primaryBrandColor: '#6E56CF',
    transformSource: (source) => {
      const urlPatterns = {
        blog: 'reflex.dev/blog',
        library: 'reflex.dev/docs/library',
        apiRef: 'reflex.dev/docs/api-reference',
        docs: 'reflex.dev/docs',
      }

      function matchUrl(pattern) {
        return source.url.includes(pattern)
      }

      function getBreadcrumbs() {
        if (matchUrl(urlPatterns.blog)) {
          return ['Blogs', ...source.breadcrumbs.slice(1)]
        }
        if (matchUrl(urlPatterns.library)) {
          return ['Components', ...source.breadcrumbs.slice(1)]
        }
        if (matchUrl(urlPatterns.apiRef)) {
          return ['API Reference']
        }
        if (matchUrl(urlPatterns.docs)) {
          return ['Docs', ...source.breadcrumbs.slice(1)]
        }
        return source.breadcrumbs
      }

      const breadcrumbs = getBreadcrumbs()

      function getTabs() {
        const tabMap = {
          [urlPatterns.blog]: 'Blogs',
          [urlPatterns.library]: 'Components',
          [urlPatterns.apiRef]: 'API Reference',
          [urlPatterns.docs]: 'Docs',
        }

        for (const [pattern, tab] of Object.entries(tabMap)) {
          if (matchUrl(pattern)) {
            return [
              ...(source.tabs ?? []),
              // If the first breadcrumb is the same as the tab, use the remaining breadcrumbs
              // This is only if you don't want breadcrumbs to include current tab, e.g. just "Blog Post" instead of "Blogs > Blog Post" in the Blogs tab
              // The tab type accepts a string or an object with a breadcrumbs property i.e. breadcrumbs shown for this source in that tab
              [
                tab,
                { breadcrumbs: breadcrumbs[0] === tab ? breadcrumbs.slice(1) : breadcrumbs },
              ],
            ]
          }
        }
        return source.tabs
      }

      return {
        ...source,
        tabs: getTabs(),
        breadcrumbs,
      }
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

            [data-theme='light'] .ikp-search-bar__container,
            [data-theme='dark'] .ikp-search-bar__container {
              display: flex;
              justify-content: center;
              align-items: center;
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
    }
  },
  searchSettings: { // optional InkeepSearchSettings
    tabs: ['All', 'Docs', 'Components', 'API Reference', 'Blogs', 'GitHub', 'Forums'].map((t) => [
      t,
      { isAlwaysVisible: true },
    ]),
    placeholder: 'Search',
  },
  aiChatSettings: { // optional typeof InkeepAIChatSettings
    exampleQuestions: [
      'How does Reflex work?',
      'What types of apps can I build with Reflex?',
      'Where can I deploy my apps?',
    ],
    getTools: () => [
      {
        type: "function",
        function: {
          name: "provideAnswerConfidence",
          description: "Determine how confident the AI assistant was and whether or not to escalate to humans.",
          parameters: escalationParams,
        },
        renderMessageButtons: ({ args }) => {
          const confidence = args.answerConfidence;
          if (["not_confident", "no_sources", "other"].includes(confidence)) {
            return [
              {
                label: "Contact Support",
                action: {
                  'type': 'open_form',
                },
              }
            ];
          }
          return [];
        },
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
