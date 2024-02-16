from chain.apps import ChainConfig
from rest_framework.routers import DefaultRouter

from chain.views.partner import PartnerViewSet
from chain.views.product import ProductViewSet

app_name = ChainConfig.name

router = DefaultRouter()
router.register(r'partner', PartnerViewSet, basename='partner')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [

] + router.urls
