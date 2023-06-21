from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
from datetime import date, timedelta, datetime


class ClassValidationMixin:

    def __init__(self):
        self.update = False

    def validate(self, request_data, user_pk, request, qs):
        checklist = [
            self.validate_request_user,
            self.validate_date,
            self.validate_time_end_greater,
            self.validate_class_overlap,
            self.validate_class_time_borders,
            self.validate_straight_hour,
            self.validate_lesson_duration,
        ]
        for validator in checklist:
            response = validator(request_data, user_pk, request, qs)
            if response:
                return response

    def validate_request_user(self, request_data, user_pk, request, qs):
        try:
            if request.user.pk != request_data.get("teacher").pk:
                return Response(status=HTTP_400_BAD_REQUEST)
        except AttributeError:
            self.update = True
            if request.user.pk != request_data.get("teacher"):
                return Response(status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def validate_date(request_data, user_pk, request, qs):
        print(request_data.get("date"))
        if request_data.get("date") < date.today():
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data="Can not create lessons for past days!",
            )

    @staticmethod
    def validate_class_overlap(request_data, user_pk, request, qs):
        start = request_data.get("time_start")
        end = request_data.get("time_end")
        qs = qs.filter(date=request_data.get("date")).filter(teacher__pk=user_pk)
        for lesson in qs:
            if all((lesson.time_start == start, lesson.time_end == end)):
                return Response(
                    status=HTTP_409_CONFLICT,
                    data="Can not create two lessons overlapping!",
                )

    @staticmethod
    def validate_class_time_borders(request_data, user_pk, request, qs):
        start = request_data.get("time_start")
        end = request_data.get("time_end")
        qs = qs.filter(date=request_data.get("date")).filter(teacher__pk=user_pk)
        inst_pk = request_data.get('inst_pk', None)
        print(request_data)
        for lesson in qs:
            if not inst_pk:
                if not all(
                    (
                        start < lesson.time_start or lesson.time_end <= start,
                        end <= lesson.time_start or lesson.time_end < end,
                    )
                ):
                    return Response(
                        status=HTTP_409_CONFLICT,
                        data="Can not create two lessons if any time border in other lesson!",
                    )
            else:
                if not all(
                    (
                            (start < lesson.time_start and lesson.pk == inst_pk)
                            or (lesson.time_end <= start and lesson.pk == inst_pk),

                            (end <= lesson.time_start and lesson.pk == inst_pk)
                            or (lesson.time_end < end and lesson.pk == inst_pk),
                    )
                ):
                    return Response(
                        status=HTTP_409_CONFLICT,
                        data="Can not create two lessons if any time border in other lesson!",
                    )


    @staticmethod
    def validate_time_end_greater(request_data, user_pk, request, qs):
        start = request_data.get("time_start")
        end = request_data.get("time_end")
        if not end > start:
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data="End time must be greater than start time!",
            )

    @staticmethod
    def validate_straight_hour(request_data, user_pk, request, qs):
        start = request_data.get("time_start")
        end = request_data.get("time_end")
        if any(
            (
                start.minute not in (0, 30),
                end.minute not in (0, 30)
            )
        ):
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data="Time minutes must be either 0 or 30 e.g. (19:30, 14:00)",
            )

    @staticmethod
    def validate_lesson_duration(request_data, user_pk, request, qs):
        start = request_data.get("time_start")
        end = request_data.get("time_end")
        date = request_data.get("date")
        if datetime.combine(date, end) - datetime.combine(date, start) not in (
            timedelta(hours=1),
            timedelta(hours=1, minutes=30),
            timedelta(hours=2),
        ):
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data="Lesson duration must be exact 1 hour, 1,5 hours or 2 hours",
            )
