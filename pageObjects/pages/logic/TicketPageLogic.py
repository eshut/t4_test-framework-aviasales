from framework.utils import ElementOperations
import random
import re

class logic:
    def checkValues(self, tickets):
        x = []
        for elem in tickets:
            text = elem.text
            pattern = "\\d+"
            ticket = re.findall(pattern, text)
            try:
                lastx = x[-1].text
                lastt = re.findall(pattern, lastx)
                if int(ticket) < int(lastt):
                    x.append(elem)
            except:
                x.append(elem)

        return x[0]