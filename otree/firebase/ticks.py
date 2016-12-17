def collect_ticks(decisions):
    ticks = []
    for decision in decisions:
        ticks.append({
            'timestamp': decision.timestamp,
            'session': decision.session,
            'app': decision.app,
            'subsession': decision.subsession,
            'round': decision.round,
            'group': decision.group,
            'page': decision.page,
            'component': decision.component,
            'participant': decision.participant.code,
            'decision': decision.decision
        })
    return [
        'timestamp',
        'session',
        'app',
        'subsession',
        'round',
        'group',
        'page',
        'component',
        'participant',
        'decision'
    ], ticks
