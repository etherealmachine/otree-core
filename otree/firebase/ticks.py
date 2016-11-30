def collect_ticks(decisions):
    ticks = []
    for decision in decisions:
        ticks.append({
            'timestamp': decision.timestamp,
            'component': decision.component,
            'session': decision.session,
            'subsession': decision.subsession,
            'round': decision.round,
            'group': decision.group,
            'participant': decision.participant.code,
            'decision': decision.decision
        })
    return [
        'timestamp',
        'component',
        'session',
        'subsession',
        'round',
        'group',
        'participant',
        'decision'
    ], ticks
