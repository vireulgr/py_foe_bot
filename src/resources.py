import sys

resourcesPath = './Resources'

battleResources = resourcesPath + '/img/battle'
socialResources = resourcesPath + '/img/social'

imgPatterns = {
    'social': {
        'buttons': {
            'minimize':     socialResources + '/buttons/minimize.png',
            'maximize':     socialResources + '/buttons/maximize.png',
            'start':        socialResources + '/buttons/start.png',
            'end':          socialResources + '/buttons/end.png',
            'left':         socialResources + '/buttons/left.png',
            'right':        socialResources + '/buttons/right.png',
            'far_left':     socialResources + '/buttons/far_left.png',
            'far_right':    socialResources + '/buttons/far_right.png',
            'friends_active':   socialResources + '/buttons/friends_active.png',
            'friends_inactive': socialResources + '/buttons/friends_inactive.png',
        },
        'player': {
            'tavern_ready': socialResources + '/player/tavern_ready.png',
            'tavern_wait':  socialResources + '/player/tavern_wait.png',
            'buff':         socialResources + '/player/buff.png',
            'number_one_list': [
                socialResources + '/player/number_one_0.png',
                socialResources + '/player/number_one_1.png',
            ]
            # 'portrait': resourcesPath + 'img/social/player/tavern.png',
            # 'message': resourcesPath + 'img/social/player/message.png',
            # 'greatBuildings': resourcesPath + 'img/social/player/greatBuildings.png',
        },
    },
    'battle': {
        'title': battleResources + '/manage_army_title.png',
    }
}


def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv)
