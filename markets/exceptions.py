from django.utils.translation import ugettext_lazy as _


class MarketBaseError(Exception):
    """ Prediction market base exception """

    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class NotEnoughCash(MarketBaseError):
    def __init__(self):
        super().__init__(msg=_('User has not enough cash.'))


class NotEnoughAssetAmount(MarketBaseError):
    def __init__(self):
        super().__init__(msg=_('Asset has not enough amount.'))
