import os


DJANGO_TELEGRAMBOT = {

    'MODE': 'POLLING',

    'BOTS': [
        {
            'TOKEN': os.getenv('BOT_TOKEN'),
            'PROXY': {
                'proxy_url': os.getenv('PROXY_URL'),
            }
        },
    ],

}
