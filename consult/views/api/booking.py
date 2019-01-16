import datetime

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from cotidia.admin.mixins import StaffPermissionRequiredMixin

from consult.models import Booking
from consult.serializers import BookingCalendarSerializer


class BookingCalendarAPIView(ListAPIView):
    permission_classes = (StaffPermissionRequiredMixin,)
    permission_required = ["consult.add_booking", "consult.change_booking"]

    def get_queryset(self):
        return Booking.objects.filter().order_by("datetime")

    def get_serializer_class(self):
        return BookingCalendarSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Cache callsheet and client
        queryset = queryset.select_related("customer")

        start_date = None

        #
        # Filter by date range
        #
        # Date range values
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if start_date and end_date:
            try:
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            except Exception:
                return Response(
                    {
                        "message": "The start date format is invalid. Required: YYYY-MM-DD"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            except Exception:
                return Response(
                    {"message": "The end date format is invalid. Required: YYYY-MM-DD"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            queryset = queryset.filter(datetime__range=(start_date, end_date))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
