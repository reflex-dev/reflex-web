"""UI and logic inkeep chat component."""
import os
from datetime import datetime
from typing import Any, Optional, Set

import requests
from sqlmodel import Field

import reflex as rx
from pcweb import constants, styles
from pcweb.components.logo import navbar_logo
from reflex.vars import ImportVar, Var

class Search(rx.Component):
    tag = "InkeepEmbeddedChat"

    library = "@inkeep/widgets@latest"

    special_props: Set[Var] = {Var.create_safe("{...inkeepEmbeddedChatProps}")}

    is_open: Var[bool] = False

    def _get_imports(self):
        return {"next/dynamic": {ImportVar(tag="dynamic", is_default=True)}}

    def get_event_triggers(self) -> dict[str, Any]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            **super().get_event_triggers(),
            "on_close": lambda: [],
            "on_shortcutKey_pressed": lambda: [],
        }

    def _get_custom_code(self) -> str:
        return """ 
const InkeepEmbeddedChat = dynamic(() => import("@inkeep/widgets").then((mod) => mod.InkeepEmbeddedChat), { ssr: false });

const inkeepEmbeddedChatProps = {
  baseSettings: {
    apiKey: '87b7469f79014c35a3313795088151a52de8a58a547abd16',
    integrationId: 'clkbf9e7e0001s601sa0ciax1',
    organizationId: 'org_WQKeNdnuPGEfuUhC',
    organizationDisplayName: 'Reflex',
    primaryBrandColor: '#5646ED',
    theme: {
        primaryColors: {
        textColorOnPrimary: '#11181c',
        textBold: '#141d20',
        textSubtle: '#354a51',
        lighter: '#e5feff',
        light: '#85f0ff',
        lightSubtle: '#f1f8fa',
        medium: '#26d6ff', // primaryBrandColor
        strong: '#00b5dd',
        stronger: '#006881',
        hitContentPreview: '#00b5dd',
        hitContentPreviewHover: '#006881',
        textColorOnPrimary: 'white',
        },
    },
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
          breadcrumbName: 'Components Reference',
        },
      ],
    },
    stringReplacementRules: [
      {
        matchingRule: {
          ruleType: 'Substring',
          string: 'Api',
        },
        replaceWith: 'API',
        replaceInTitles: true,
      },
      {
        matchingRule: {
          ruleType: 'Substring',
          string: 'Cli',
        },
        replaceWith: 'CLI',
        replaceInTitles: true,
      },
    ],
    theme: {
      components: {
        AIChatPageWrapper: {
          defaultProps: {
            variant: '',
            size: 'expand',
          },
        },
      }
    },
  },
  aiChatSettings: { // optional typeof InkeepAIChatSettings
    botName: 'Reflex AI',
    quickQuestions: [
      'How does Reflex work?',
      'What types of apps can I build with Reflex?',
      'Where can I deploy my apps?',
    ],
  },
};
"""


inkeep = Search.create

