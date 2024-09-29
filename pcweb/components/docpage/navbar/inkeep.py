"""UI and logic inkeep chat component."""

import itertools
from typing import List, Set

import reflex as rx
from reflex.event import EventHandler
from reflex.utils.imports import ImportVar
from reflex.vars import Var

JS_SNIPPET_INKEEP_SEARCH: str = """const SearchBar = dynamic(
  () => import('@inkeep/uikit').then((mod) => mod.InkeepSearchBar),
  {
    ssr: false,
  },
);
const searchBarProps = {
  stylesheetUrls: ['/inkeepstyle-docs.css'],
  baseSettings: {
    apiKey: 'reflex_inkeep_api_key',
    integrationId: 'refelx_inkeep_integration_id',
    customIcons: {search: {custom: "/icons/search.svg"}},
    organizationId: 'reflex_inkeep_organization_id',
    organizationDisplayName: 'reflex_inkeep_organization_display_name',
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
};"""

REFLEX_INKEEP_API_KEY: str = "87b7469f79014c35a3313795088151a52de8a58a547abd16"
REFLEX_INKEEP_INTEGRATION_ID: str = "clkbf9e7e0001s601sa0ciax1"
REFLEX_INKEEP_ORORGANIZATION_ID: str = "org_WQKeNdnuPGEfuUhC"
REFLEX_INKEEP_ORGANIZATION_DISPLAY_NAME: str = "Reflex"


def get_js_snippet_inkeep_search() -> str:
    replacements: tuple[tuple[str, str]] = (
        (
            "reflex_inkeep_api_key",
            REFLEX_INKEEP_API_KEY,
        ),
        (
            "reflex_inkeep_integration_id",
            REFLEX_INKEEP_INTEGRATION_ID,
        ),
        (
            "reflex_inkeep_organization_id",
            REFLEX_INKEEP_ORORGANIZATION_ID,
        ),
        (
            "reflex_inkeep_organization_display_name",
            REFLEX_INKEEP_ORGANIZATION_DISPLAY_NAME,
        ),
    )
    return itertools.reduce(
        lambda s, kv: s.replace(*kv),
        replacements,
        JS_SNIPPET_INKEEP_SEARCH,
    )


class Search(rx.Component):
    tag = "SearchBar"

    special_props: List[Var] = [
        Var.create(
            "{...searchBarProps}",
            _var_is_string=False,
        ),
    ]

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
            JS_SNIPPET_INKEEP_SEARCH,
        ]


inkeep = Search.create
