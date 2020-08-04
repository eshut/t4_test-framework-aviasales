from framework.common import jsonGetter
from framework.logger.logger import Logger
from framework.utils import LinkOperations, ElementOperations
from pageObjects.pages import MainPage, TicketsPage
import pytest
import time

logger = Logger(logger="TC-1").getlog()

SITE = jsonGetter.GetJson.getConfig("SITE")
testdata1 = jsonGetter.GetJson.getData("testdata1")
testdata2 = jsonGetter.GetJson.getData("testdata2")
testdata3 = jsonGetter.GetJson.getData("testdata3")


@pytest.mark.usefixtures("get_driver")
class TestSuite1:

    @pytest.mark.parametrize("fromC , toC",
        testdata1
    )
    def test_one(self, fromC, toC):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.Link(link=SITE).get()
        MainPage.MainPage().findTickets(fromC, toC)
        lowest = TicketsPage.Ticketspage().findTickets(0)
        assert lowest[0] == lowest[1], "The cheapest element is not first"

    @pytest.mark.parametrize("fromC , toC",
        testdata2
    )
    def test_two(self, fromC, toC):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.Link(link=SITE).get()
        MainPage.MainPage().findTickets(fromC, toC)
        TicketsPage.Ticketspage().findStraightPath()
        lowest = TicketsPage.Ticketspage().findTickets(-1)
        assert lowest[0] == lowest[1], "The cheapest element is not last"

    @pytest.mark.parametrize("fromC , toC",
        testdata3
    )
    def test_three(self, fromC, toC):
        logger.info("Trying to open url: " + SITE)
        LinkOperations.Link(link=SITE).get()
        MainPage.MainPage().findTickets(fromC, toC)
        data = TicketsPage.Ticketspage().setBagage()
        assert data[0] == data[1], "quantity of tickets with bagage are not equal tickets quantity"


