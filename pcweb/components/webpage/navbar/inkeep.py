"""UI and logic inkeep chat component."""

from typing import Set
import reflex as rx
from reflex.event import EventHandler
from reflex.vars import ImportVar, Var


class Search(rx.Component):
    tag = "SearchBar"

    special_props: Set[Var] = {
        Var.create_safe("{...searchBarProps}", _var_is_string=False)
    }

    is_open: Var[bool] = False

    on_close: EventHandler[lambda: []]

    on_shortcut_key_pressed: EventHandler[lambda: []]

    def add_imports(self):
        """Add the imports for the component."""
        return {
            "next/dynamic": {ImportVar(tag="dynamic", is_default=True)},
            "react": {ImportVar(tag="useContext")},
            "/utils/context": {ImportVar(tag="ColorModeContext")},
        }

    def add_hooks(self):
        """Add the hooks for the component."""
        return [
            "const { resolvedColorMode, toggleColorMode } = useContext(ColorModeContext)",
            """const SearchBar = dynamic(
  () => import('@inkeep/widgets').then((mod) => mod.InkeepSearchBar),
  {
    ssr: false,
  },
);

const searchBarProps = {
  stylesheetUrls: ['/inkeepstyle.css'],
  baseSettings: {
    apiKey: '87b7469f79014c35a3313795088151a52de8a58a547abd16',
    integrationId: 'clkbf9e7e0001s601sa0ciax1',
    organizationId: 'org_WQKeNdnuPGEfuUhC',
    organizationDisplayName: 'Reflex',
    primaryBrandColor: '#5646ED',
    customIcons: {search: {custom: "/search.svg"}},
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
      forcedColorMode: 'dark', // options: 'light' or dark'
    }, 
    theme: {
      components: {
        SearchBarTrigger: {
          defaultProps: {
            variant: 'emphasized', // 'emphasized' 'subtle'
          },
        },
      }
    }
  },
  searchSettings: { // optional InkeepSearchSettings
    tabSettings: {
      isAllTabEnabled: true,
      useAllRootBreadcrumbsAsTabs: true,
      rootBreadcrumbsToUseAsTabs: ['All', 'Docs', 'Components', 'API Reference', 'Blogs'],
      tabOrderByLabel: ['All', 'Docs', 'Components', 'API Reference', 'Blogs'],
    },
    placeholder: 'Search...',
  },
  aiChatSettings: { // optional typeof InkeepAIChatSettings
    quickQuestions: [
      'How does Reflex work?',
      'What types of apps can I build with Reflex?',
      'Where can I deploy my apps?',
    ],
  },
};""",
        ]


inkeep = Search.create
