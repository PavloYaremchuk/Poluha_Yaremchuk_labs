from django.shortcuts import render

from myapp1.repositories.context import Context


def index_page(request):
    context = Context()

    print(context.stadium_repository.get(1))

    print(context.player_repository.all())

    '''
    context.team_repository.create(
        team_name='Magic',
        year_of_start=1990,
        stadium=stadium1
    )
    '''

    context.team_repository.update(
        pk=1,
        team_name='Golden State Warriors',
        year_of_start=1995,
        stadium=context.stadium_repository.get(1)
    )

    #context.team_repository.delete(4)

    print(context.team_repository.all())

    return render(request, 'index.html')
