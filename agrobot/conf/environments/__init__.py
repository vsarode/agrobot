CONFIG_MAP = {
    'prod': 'production',
    'dev': 'development'
}

def get_config(env):
    return '.'.join(['catalogservicev2', 'conf', 'environments',
                     CONFIG_MAP.get(env, env), 'Config'])
