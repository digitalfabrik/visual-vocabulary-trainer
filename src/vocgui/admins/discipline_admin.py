from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from django.utils.translation import ugettext_lazy as _

from vocgui.models import Static

class DisciplineAdmin(OrderedModelAdmin):
    """
    Admin Interface to for the Discipline module.
    Inheriting from `ordered_model.admin.OrderedModelAdmin`.
    """

    exclude = ("creator_is_admin",)
    readonly_fields = ("created_by",)
    search_fields = ["title"]
    actions = ["delete_selected", "make_released", "make_unreleased"]
    list_display = ("title", "released", "creator_group", "move_up_down_links")
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        """
        Overwrite django built-in function to save
        user group and admin satus of model

        :param request: current user request
        :type request: django.http.request
        :param obj: discipline object
        :type obj: models.Discipline
        :param form: employed model form
        :type form: ModelForm
        :param change: True if change on existing model
        :type change: bool
        :raises IndexError: Error when user is not superuser and doesn't belong to any group
        """
        if not change:
            if len(request.user.groups.all()) >= 1:
                obj.created_by = request.user.groups.all()[0]
            elif not request.user.is_superuser:
                raise IndexError("No group assigned. Please add the user to a group")
            obj.creator_is_admin = request.user.is_superuser
        obj.save()

    def get_action_choices(self, request):
        """
        Overwrite django built-in function to modify action choices. The first
        option is dropped since it is a place holder.

        :param request: current user request
        :type request: django.http.request
        :return: modified action choices
        :rtype: dict
        """
        choices = super(DisciplineAdmin, self).get_action_choices(request)
        choices.pop(0)
        return choices

    def get_queryset(self, request):
        """
        Overwrite django built-in function to modify queryset according to user.
        Users that are not superusers only see disciplines of their groups.

        :param request: current user request
        :type request: django.http.request
        :return: adjustet queryset
        :rtype: QuerySet
        """
        qs = super(DisciplineAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by__in=request.user.groups.all())

    @admin.action(description=_("Release selected disciplines"))
    def make_released(self, request, queryset):
        """
        Action to release discipline objects. It sets the
        corresponding boolean field to true.

        :param request: current user request
        :type request: django.http.request
        :param queryset: current queryset
        :type queryset: QuerySet
        """
        queryset.update(released=True)

    @admin.action(description=_("Unrelease selected disciplines"))
    def make_unreleased(self, request, queryset):
        """
        Action to hide discipline objects. It sets the
        corresponding boolean field to false.

        :param request: current user request
        :type request: django.http.request
        :param queryset: current queryset
        :type queryset: QuerySet
        """
        queryset.update(released=False)

    def creator_group(self, obj):
        """
        Include creator group of discipline in list display

        :param obj: Discipline object
        :type obj: models.Discipline
        :return: Either static admin group or user group
        :rtype: str
        """
        if obj.creator_is_admin:
            return Static.admin_group
        elif obj.created_by:
            return obj.created_by
        else:
            return None

    creator_group.short_description = _("creator group")

