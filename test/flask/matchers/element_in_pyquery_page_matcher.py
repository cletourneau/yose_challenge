from hamcrest.core.base_matcher import BaseMatcher


class ElementInPyQueryPageMatcher(BaseMatcher):
    def __init__(self, page):
        super(ElementInPyQueryPageMatcher, self).__init__()
        self.page = page

    def _matches(self, selector):
        self.selector = selector
        return len(self.page(selector)) > 0

    def describe_to(self, description):
        description.append_text("element '{selector}' in page".format(selector=self.selector))

    def describe_mismatch(self, selector, mismatch_description):
        mismatch_description.append_text(self.page.html())


def is_in_page(page):
    return ElementInPyQueryPageMatcher(page)