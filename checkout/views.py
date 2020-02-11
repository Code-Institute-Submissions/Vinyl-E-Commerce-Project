from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm, OrderForm
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from products.models import Vinyl
import stripe
from .models import OrderLineVinyl
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET