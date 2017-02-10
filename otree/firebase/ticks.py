from collections import defaultdict

def collect_ticks(decisions):
    ticks = []
    sessions = defaultdict(lambda: {
      'rounds': defaultdict(lambda: []),
      'participants': set()
    })
    for decision in decisions:
      sessions[decision.session]['rounds'][decision.round].append(decision)
      sessions[decision.session]['participants'].add(decision.participant)

    for session_name, session in sessions.items():
      rounds = session['rounds']
      participants = session['participants']
      for roundno, decisions in rounds.items():
        duration = decisions[len(decisions)-1].timestamp - decisions[0].timestamp
        last_decision = {}
        for tick in range(duration.seconds + 1):
          for participant in participants:
            ticks.append({
              'tick': tick,
              'participant': participant.code,
              'decision': 0.5,
              'session': session_name,
              'subsession': 0,
              'round': roundno,
              'group': 0
            })
    return [
        'tick',
        'session',
        'subsession',
        'round',
        'group',
        'participant',
        'decision'
    ], ticks
