import justpy as jp

from examples import (
    hello,
    handling_events,
)

pages = [
    hello.hello_world,
    hello.hello_world_02,

    handling_events.handling_events_01,
    handling_events.handling_events_02,
    handling_events.handling_events_03,
    handling_events.handling_events_04,
]


def init_route():
    for page in pages:
        path = f"/{page.__name__}"
        jp.Route(path, page)


async def home():
    wp = jp.QuasarPage(dark=True)
    d = jp.Div(classes="q-pa-md", a=wp)
    jp.P(classes="text-h2 text-center", text="Welcome to JustPy examples", a=d)

    def redirect(self, msg):
        msg.page.redirect = self.text

    list_menu = jp.QList(dense=True, bordered=True, padding=True, a=d)
    for page in pages:
        item_menu = jp.QItem(clickable=True, v_ripple=True, a=list_menu)
        path = f"/{page.__name__}"
        item_selection = jp.QItemSection(text=path, a=item_menu)
        item_selection.on('click', redirect)

    return wp


init_route()
jp.Route("/", home)
jp.justpy()
