from django.shortcuts import render, redirect

class ObjListMix:
    model = None
    template = None

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, context={self.model.__name__.lower(): obj})

class ObjDetMix:
    model = None
    template = None
    com = False


    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        con = None
        comment_list = None
        if self.com:
            con = {self.model.__name__.lower(): obj}
            comment_list = obj.comment_set.order_by('-id')
            con['comments'] = comment_list
            return con
        else:
            con = {self.model.__name__.lower(): obj}
            return con

        return render(request, self.template, context=con)

class ObjCreateMix:
    form = None
    template = None

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request, self.template, context={'form': bound_form})


class ObjEditMix:
    model = None
    form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form(instance=obj)
        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjDeleteMix:
    model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()


