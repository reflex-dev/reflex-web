import reflex as rx


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    class_name="absolute inset-0 -z-10 h-full w-full bg-white bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h1(
                                rx.el.span(
                                    "The future of", class_name="block text-gray-900"
                                ),
                                rx.el.span(
                                    "finance is", class_name="block text-gray-900"
                                ),
                                rx.el.span(
                                    "Python, Data, and AI",
                                    class_name="block text-transparent bg-clip-text bg-gradient-to-r from-violet-600 via-purple-600 to-indigo-600",
                                ),
                                class_name="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight leading-[1.1] mb-8",
                            ),
                            rx.el.p(
                                "Give quants, risk teams, and operations the power to build production-grade dashboards and AI tools in pure Python—without waiting on front-end teams.",
                                class_name="text-xl text-gray-600 font-medium mb-10 leading-relaxed max-w-2xl",
                            ),
                            rx.el.div(
                                rx.el.a(
                                    "Talk to a solutions engineer",
                                    rx.icon(
                                        "messages-square", class_name="h-5 w-5 ml-2"
                                    ),
                                    href="https://cal.com/team/reflex/demo-call-1",
                                    target="_blank",
                                    class_name="flex items-center justify-center w-full sm:w-auto bg-violet-600 hover:bg-violet-700 text-white px-8 py-4 rounded-xl text-base font-semibold transition-all duration-200 shadow-sm hover:shadow-md hover:-translate-y-0.5 cursor-pointer",
                                ),
                                rx.el.a(
                                    "Book a financial services demo",
                                    rx.icon("calendar", class_name="h-5 w-5 ml-2"),
                                    href="https://cal.com/team/reflex/reflex-intro",
                                    target="_blank",
                                    class_name="flex items-center justify-center w-full sm:w-auto bg-white text-gray-700 border border-gray-200 hover:border-violet-200 hover:bg-gray-50 px-8 py-4 rounded-xl text-base font-semibold transition-all duration-200 shadow-sm hover:shadow-md hover:-translate-y-0.5 cursor-pointer",
                                ),
                                class_name="flex flex-col sm:flex-row items-start gap-4 w-full",
                            ),
                            class_name="flex flex-col items-start justify-center lg:pr-12 lg:col-span-3",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        "zap", class_name="h-6 w-6 text-violet-600 mb-2"
                                    ),
                                    rx.el.h3(
                                        "Why Reflex?",
                                        class_name="text-sm font-bold uppercase tracking-wider text-violet-600 mb-3",
                                    ),
                                    class_name="flex flex-col items-start mb-2",
                                ),
                                rx.el.p(
                                    "Reflex helps banks, asset managers, fintechs, and hedge funds build secure internal tools and data apps up to 10x faster in pure Python.",
                                    class_name="text-lg text-gray-700 mb-4 leading-relaxed",
                                ),
                                rx.el.p(
                                    "Teams ship everything from risk dashboards and model validation portals to AI-powered RAG chatbots, all without leaving Python, from prototype to production.",
                                    class_name="text-lg text-gray-700 leading-relaxed",
                                ),
                                class_name="bg-white/60 backdrop-blur-xl border border-gray-100 p-8 rounded-2xl shadow-lg",
                            ),
                            class_name="flex items-center justify-center lg:pl-4 mt-16 lg:mt-0 w-full lg:col-span-2",
                        ),
                        class_name="grid grid-cols-1 lg:grid-cols-5 gap-12 items-center pt-32 pb-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto relative z-10",
                    ),
                    class_name="relative w-full max-w-[1440px] mx-auto",
                ),
                rx.el.div(
                    class_name="absolute top-0 right-0 -z-10 w-[800px] h-[800px] bg-radial-gradient from-violet-100/40 to-transparent opacity-60 blur-3xl rounded-bl-full"
                ),
                rx.el.div(
                    class_name="absolute top-[200px] left-[-200px] -z-10 w-[600px] h-[600px] bg-radial-gradient from-purple-100/40 to-transparent opacity-50 blur-3xl rounded-tr-full"
                ),
            ),
            class_name="relative w-full overflow-hidden",
        ),
        class_name="w-full",
    )


def logo_item(name: str, icon_name: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon_name, class_name="h-6 w-6 mr-2 opacity-50"),
        rx.el.span(
            name,
            class_name="text-lg font-bold tracking-tight text-gray-500 group-hover:text-gray-800 transition-colors",
        ),
        class_name="flex items-center opacity-60 grayscale hover:grayscale-0 hover:opacity-100 transition-all duration-300 cursor-default group",
    )


def logo_row() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.p(
                "TRUSTED BY INNOVATIVE FINANCE TEAMS AT",
                class_name="text-center text-xs font-bold tracking-[0.2em] text-gray-400 mb-8 uppercase",
            ),
            rx.el.div(
                logo_item("Man Group", "bar-chart-2"),
                logo_item("Crédit Agricole CIB", "building-2"),
                logo_item("Bayesline", "network"),
                logo_item("World Bank", "globe"),
                class_name="flex flex-wrap justify-center gap-x-12 gap-y-8 items-center max-w-5xl mx-auto px-6",
            ),
            class_name="border-y border-gray-100 bg-white/50 py-12 backdrop-blur-sm",
        ),
        class_name="w-full",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-7 w-7 text-violet-600"),
            class_name="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-xl bg-violet-50/80",
        ),
        rx.el.h3(
            title, class_name="mb-3 text-lg font-bold text-gray-900 tracking-tight"
        ),
        rx.el.p(description, class_name="text-base leading-relaxed text-gray-600"),
        class_name="group relative rounded-2xl border border-gray-200/60 bg-white p-8 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-md hover:border-violet-100",
    )


def features_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Balance resilience and innovation",
                    class_name="text-3xl font-extrabold text-gray-900 sm:text-4xl mb-4",
                ),
                rx.el.p(
                    "Financial organizations are under pressure from every side: volatile markets, new regulations, GenAI, and rising expectations. Most internal tools haven't kept up.",
                    class_name="mx-auto max-w-2xl text-lg text-gray-600",
                ),
                class_name="mb-16 text-center max-w-3xl mx-auto",
            ),
            rx.el.div(
                feature_card(
                    "shield-check",
                    "Ship AI-powered tools securely",
                    "Build chat-based assistants and RAG apps in Python, deployed inside your own cloud or on-prem, with full control over where data lives.",
                ),
                feature_card(
                    "refresh-cw",
                    "Modernize legacy internal apps",
                    "Replace fragile in-house dashboards with maintainable Python apps that plug into your existing data stack.",
                ),
                feature_card(
                    "workflow",
                    "Automate workflows, not just reports",
                    "Turn manual compliance checks, KYC workflows, and operations processes into interactive apps—tied to your systems, not screenshots.",
                ),
                feature_card(
                    "layers",
                    "Orchestrate end-to-end lifecycles",
                    "Let researchers, analysts, and quants move from 'run a script in a Jupyter notebook' to 'share a full app' using the same language they already know.",
                ),
                class_name="grid gap-8 md:grid-cols-2 lg:grid-cols-4",
            ),
            class_name="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8",
        ),
        class_name="bg-white w-full",
    )


def case_study_card(
    company: str,
    title: str,
    subheading: str,
    body: str,
    quote: str,
    icon: str,
    theme_color: str = "violet",
) -> rx.Component:
    color_class = (
        "violet" if theme_color in ["sky", "blue", "indigo", "teal"] else theme_color
    )
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name=f"h-8 w-8 text-{color_class}-600 mb-4"),
                rx.el.span(
                    company,
                    class_name=f"inline-block rounded-full bg-{color_class}-50 px-3 py-1 text-xs font-bold uppercase tracking-wider text-{color_class}-600 mb-5 border border-{color_class}-100",
                ),
                class_name="flex flex-col items-start",
            ),
            rx.el.h3(
                title, class_name="mb-3 text-2xl font-bold text-gray-900 tracking-tight"
            ),
            rx.el.p(
                subheading,
                class_name=f"mb-5 text-sm font-bold text-{color_class}-600 uppercase tracking-wide",
            ),
            rx.el.p(body, class_name="mb-8 text-gray-600 leading-relaxed"),
            rx.el.blockquote(
                rx.el.p(f'"{quote}"', class_name="italic text-gray-800 font-medium"),
                class_name=f"border-l-2 border-{color_class}-500 bg-gray-50/50 p-5 rounded-r-lg",
            ),
            class_name="flex-grow",
        ),
        class_name="flex flex-col h-full rounded-2xl border border-gray-200 bg-white p-8 shadow-sm transition-all duration-300 hover:shadow-lg hover:-translate-y-1 hover:border-violet-100",
    )


def case_studies_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Proven at the world's leading institutions",
                    class_name="text-3xl font-extrabold text-gray-900 sm:text-4xl mb-4 tracking-tight",
                ),
                rx.el.p(
                    "From global banks to agile fintechs, see how teams are transforming their internal tools with Reflex.",
                    class_name="mx-auto max-w-2xl text-lg text-gray-600 mb-20",
                ),
                class_name="text-center max-w-3xl mx-auto",
            ),
            rx.el.div(
                case_study_card(
                    company="Crédit Agricole CIB",
                    title="Automate analytics for internal AI tools",
                    subheading="Deploy bank-grade internal dashboards in days, not months",
                    body="Léo's R&D team turned a rough prototype into a production-grade dashboard tracking usage of a GPT-powered internal chatbot. What used to require weeks of front-end work now ships in a couple of days, inside their internal AWS environment.",
                    quote="It's like comparing a bike to a supercar. (Comparing Dash to Reflex)",
                    icon="building-2",
                ),
                case_study_card(
                    company="Man Group - AHL",
                    title="Self-service dashboards in pure Python",
                    subheading="Empower 50+ researchers with a Python-native platform",
                    body="Man Group's AHL division is rebuilding its internal model validation platform so 50+ PhD-level researchers can create dashboards directly in Python, kept fully offline in air-gapped environments with no SaaS dependencies.",
                    quote="The ideal state is researchers write high-level Python and get a dashboard — and Reflex gets us very close to that.",
                    icon="bar-chart-2",
                    theme_color="indigo",
                ),
                case_study_card(
                    company="World Bank",
                    title="Replace brittle prototypes with production apps",
                    subheading="Go straight from idea to production",
                    body="Teams were stuck jumping between Tableau, Streamlit, and custom JS. With Reflex, they're building production-grade data platforms from day one, including an AI-powered legal assistant used by 100+ lawyers.",
                    quote="You wouldn't want to use Dash or Streamlit to build a real production-grade app... We have them go straight into Reflex.",
                    icon="globe",
                    theme_color="blue",
                ),
                case_study_card(
                    company="Bayesline",
                    title="Ship fintech-grade SaaS without a front-end team",
                    subheading="From YC prototype to fintech SaaS",
                    body="Bayesline's founders built a full risk analytics platform on Reflex—wrapping AG Grid and handling 100k+ instruments. They achieved ~4x faster development vs React and wrote 50% less code than their previous Dash implementation.",
                    quote="Using Reflex instead of Plotly Dash was like the difference between organized Legos and a plate of spaghetti.",
                    icon="network",
                    theme_color="teal",
                ),
                class_name="grid gap-8 md:grid-cols-2",
            ),
            class_name="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-50/50 w-full border-y border-gray-200/60",
    )


def pillar_card(label: str, title: str, body: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-violet-600"),
            class_name="mb-6 inline-flex h-12 w-12 items-center justify-center rounded-lg bg-violet-50",
        ),
        rx.el.div(
            rx.el.span(
                label,
                class_name="mb-2 block text-xs font-bold uppercase tracking-wider text-violet-600",
            ),
            rx.el.h3(
                title, class_name="mb-3 text-lg font-bold text-gray-900 tracking-tight"
            ),
            rx.el.p(body, class_name="text-base leading-relaxed text-gray-600"),
        ),
        class_name="flex flex-col rounded-2xl border border-gray-200/60 bg-white p-8 shadow-sm transition-all duration-300 hover:shadow-lg hover:border-violet-100 hover:-translate-y-1",
    )


def pillars_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Why financial organizations choose Reflex",
                    class_name="text-3xl font-extrabold text-gray-900 sm:text-4xl mb-12 text-center",
                ),
                class_name="max-w-7xl mx-auto",
            ),
            rx.el.div(
                pillar_card(
                    label="Speed to production",
                    title="Ship internal tools 10x faster",
                    body="Reflex lets Python teams build production-grade apps without leaving their language. Crédit Agricole’s R&D team built a full chatbot analytics dashboard in two days and is rolling it out to 100+ users, without adding a single React engineer.",
                    icon="zap",
                ),
                pillar_card(
                    label="Python-first flexibility",
                    title="Let experts build, not just consume",
                    body="At Man Group, 50+ researchers write Python, not JavaScript. Reflex gives them a full-Python framework to create dashboards and model views without touching javascript front-end code, while the platform team wraps their internal design system.",
                    icon="code-2",
                ),
                pillar_card(
                    label="Full control & enterprise deployment",
                    title="Run in your cloud, offline if needed",
                    body="Reflex Enterprise runs fully on-prem or in your own cloud. Man Group deploys Reflex apps in air-gapped environments; CACIB and the World Bank run Reflex inside internal AWS and Azure environments with their own SSO, logging, and infra.",
                    icon="shield-check",
                ),
                pillar_card(
                    label="Agility & cost efficiency",
                    title="Do more with your Python team",
                    body="Bayesline avoided hiring a front-end engineer and shipped a fintech SaaS app entirely in Python; One engineer can do the work of two by collapsing front- and back-end into a single Reflex codebase.",
                    icon="trending-up",
                ),
                class_name="grid gap-8 md:grid-cols-2 lg:grid-cols-4",
            ),
            class_name="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-50 w-full border-t border-gray-200",
    )


def stat_item(metric: str, description: str, subtext: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            metric,
            class_name="text-4xl sm:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-violet-600 to-purple-600 mb-3",
        ),
        rx.el.div(description, class_name="text-lg font-bold text-gray-900 mb-1"),
        rx.el.div(subtext, class_name="text-sm text-gray-500 font-medium"),
        class_name="flex flex-col items-center text-center p-8",
    )


def stats_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Reflex as a strategic platform for Finance Teams",
                    class_name="text-3xl font-extrabold text-gray-900 sm:text-4xl mb-16 text-center",
                ),
                rx.el.div(
                    stat_item(
                        "10x",
                        "Faster Development",
                        "vs legacy front-end stacks (Crédit Agricole CIB)",
                    ),
                    stat_item(
                        "50+",
                        "Quant Researchers",
                        "building dashboards in Python (Man Group)",
                    ),
                    stat_item(
                        "100+",
                        "Legal Professionals",
                        "using AI tools replacing Tableau (World Bank)",
                    ),
                    stat_item(
                        "4x",
                        "Faster & 50% Less Code",
                        "vs Dash/React for fintech analytics (Bayesline)",
                    ),
                    class_name="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4 divide-y sm:divide-y-0 sm:divide-x divide-gray-100",
                ),
                class_name="max-w-7xl mx-auto",
            ),
            class_name="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8",
        ),
        class_name="bg-white w-full border-t border-gray-200",
    )


def cta_block(
    title: str, description: str, button_text: str, href: str, is_primary: bool = True
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                title, class_name="text-2xl font-bold text-gray-900 mb-4 tracking-tight"
            ),
            rx.el.p(
                description, class_name="text-lg text-gray-600 mb-8 leading-relaxed"
            ),
            rx.el.a(
                button_text,
                rx.icon("arrow-right", class_name="ml-2 h-5 w-5"),
                href=href,
                target="_blank",
                class_name=rx.cond(
                    is_primary,
                    "inline-flex items-center justify-center rounded-xl bg-violet-600 px-6 py-3 text-base font-semibold text-white shadow-sm hover:bg-violet-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-violet-600 transition-all duration-200 hover:-translate-y-0.5 cursor-pointer",
                    "inline-flex items-center justify-center rounded-xl bg-white px-6 py-3 text-base font-semibold text-gray-900 ring-1 ring-inset ring-gray-200 hover:bg-gray-50 transition-all duration-200 hover:-translate-y-0.5 cursor-pointer",
                ),
            ),
            class_name="max-w-xl",
        ),
        class_name=f"relative isolate overflow-hidden rounded-3xl px-6 py-12 shadow-lg sm:px-12 md:pt-12 lg:flex lg:gap-x-20 lg:px-16 items-center {('bg-violet-50/30 border border-violet-100' if is_primary else 'bg-white border border-gray-200')}",
    )


def cta_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                cta_block(
                    "Give us your toughest internal tool",
                    "Have a spreadsheet-driven workflow, a fragile Streamlit app, or a dashboard that never quite got to production? We’ll show you what it looks like as a Reflex app in pure Python.",
                    "Schedule demo",
                    href="https://cal.com/team/reflex/reflex-intro",
                    is_primary=True,
                ),
                cta_block(
                    "Spin up your first finance app",
                    "Connect your data source, and ship a working internal tool in an afternoon—no JavaScript required.",
                    "Go to the Builder",
                    href="https://build.reflex.dev/",
                    is_primary=False,
                ),
                class_name="grid gap-8 lg:grid-cols-2 max-w-7xl mx-auto",
            ),
            class_name="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8",
        ),
        class_name="bg-white w-full",
    )


def finance_landing_page() -> rx.Component:
    return rx.el.div(
        rx.el.main(
            hero_section(),
            logo_row(),
            features_section(),
            case_studies_section(),
            pillars_section(),
            stats_section(),
            cta_section(),
            class_name="w-full",
        ),
        class_name="font-['Instrument_Sans'] antialiased text-gray-900 bg-white selection:bg-violet-100 selection:text-violet-900 min-h-screen",
    )
