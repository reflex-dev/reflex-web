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
            "/utils/context": {ImportVar(tag="ColorModeContext")},
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
const searchBarProps = {
  stylesheetUrls: ['/inkeepstyle-docs.css'],
  baseSettings: {
    apiKey: '87b7469f79014c35a3313795088151a52de8a58a547abd16',
    integrationId: 'clkbf9e7e0001s601sa0ciax1',
    customIcons: {search: {custom: "/icons/search.svg"}},
    organizationId: 'org_WQKeNdnuPGEfuUhC',
    organizationDisplayName: 'Reflex',
    primaryBrandColor: '#6E56CF',
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
  },
};""",
        ]


inkeep = Search.create
