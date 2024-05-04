import json
import httpx
import reflex as rx
from rxconfig import config

class SideBarState(rx.State):
    """Side Bar State."""

    community_apps_list: list[dict[str, str]]
    example_apps_list: list[dict[str, str]]

    page: int = 1
    sort_by: str = "page_views"

    tags_list: list[str]
    chosen_tags: set[str]


    def set_sort_by(self, sort_by: str):
        self.sort_by = sort_by
        self.fetch_apps_list()

    def set_page(self, page: int):
        if page < 1:
            page = 1
        elif page <= (len(self.community_apps_list)//16)+1:
            self.page = page

    def update_tag(self, name: str):
        self.chosen_tags.symmetric_difference_update({name})

    def _filter_by_tag(self, apps_list: list[dict[str, str]]) -> list[dict[str, str]]:
        """This function iterates over all the apps we have and if the app has one of the
        tags we have selected in true_tags then it will render this app in the UI."""
        if not self.chosen_tags:
            return apps_list
        return [
            app
            for app in apps_list
            if set(app["keywords"] or []).intersection(self.chosen_tags)
        ]

    @rx.cached_var
    def example_apps_to_return(self) -> list[dict[str, str]]:
        """This function returns the examples apps filtered by selected tags."""
        return self._filter_by_tag(self.example_apps_list)

    @rx.cached_var
    def community_apps_to_return(self) -> list[dict[str, str]]:
        """This function returns the community apps filtered by selected tags."""
        return self.community_apps_list[(self.page-1)*16:self.page * 16]

    def fetch_apps_list(self):
        ascending=False
        
        try:
            response = httpx.get(f"{config.cp_backend_url}/deployments/gallery")
            response.raise_for_status()
            all_apps = response.json()      
        except (httpx.HTTPError, json.JSONDecodeError) as ex:
            print(
                f"Internal error: failed to fetch the complete list of apps due to: {ex}"
            )
            return

        remaining_apps = []
        for app in all_apps:
            if not app.get("is_example_app"):  # Apply the checks only for community apps
                if not app.get('hidden', False) and \
                    app.get('health_status', False) and \
                    app.get('health_status', {}).get('frontend_reachable', False) and \
                    app.get('health_status', {}).get('backend_reachable', False):
                    remaining_apps.append(app)
                else:
                    continue
            else:
                remaining_apps.append(app)  # Add non-community apps without checks

        all_apps = remaining_apps




        # Make sure all apps have a keywords field.
        for app in all_apps:
            app["keywords"] = app.get("keywords") or []
            # If the app does not have a display name, use the first part of the domain name: e.g. https://test.reflex.run -> test
            subdomain_name = app["demo_url"].replace("https://", "").split(".")[0]
            app["display_name"] = app.get("display_name") or subdomain_name

        if self.sort_by == 'page_views':
            all_apps.sort(key=lambda x: (x.get('site_visits') or {}).get('monthly', 0), reverse=not ascending)
        elif self.sort_by == 'updated_at':
            all_apps.sort(key=lambda x: x.get('updated_at') or float('-inf'), reverse=not ascending)
        elif self.sort_by == 'created_at':
            all_apps.sort(key=lambda x: x.get('created_at') or float('-inf'), reverse=not ascending)

        # Make sure reflex web is the first app in the list.
        self.example_apps_list = [
            app for app in all_apps if app.get("demo_url") == "https://reflex.dev/"
        ] + [
            app
            for app in all_apps
            if app.get("is_example_app")
            and app.get("demo_url") != "https://reflex.dev/"
        ]
        
        self.community_apps_list = [
            app for app in all_apps if not app.get("is_example_app")
        ]
        unique_tags = set() 
        for app in self.example_apps_list:
            unique_tags.update(app["keywords"] or [])

        self.tags_list = list(unique_tags)
        self.chosen_tags_dict = {key: False for key in self.tags_list}
