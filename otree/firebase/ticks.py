from collections import defaultdict
import datetime

def collect_ticks(decisions):
        """Collect decisions over time into ticks.

        Currently this gives 1 tick per second, but that could be parameterized
        if necessary.

        Note: This does not yet handle decision vectors yet - all decision
        vectors are treated as a scalar.
        """
        ticks = []
        sessions = defaultdict(lambda: {
            'rounds': defaultdict(lambda: []),
            'participants': set()
        })
        for decision in decisions:
            session = sessions[decision.session]
            session['rounds'][decision.round].append(decision)
            session['participants'].add(decision.participant)

        for session, session_data in sessions.items():
            rounds = session_data['rounds']
            participants = session_data['participants']
            round_ticks = []
            for roundno, round_decisions in rounds.items():
                start_time = round_decisions[0].timestamp
                end_time = round_decisions[-1].timestamp
                duration = end_time - start_time
                tick_end = start_time + datetime.timedelta(seconds=1)
                last_decision = {}
                tick_decisions = defaultdict(lambda: [])
                tick = 1
                for decision in round_decisions:
                    last_decision[decision.participant.code] = decision
                    tick_decisions[decision.participant.code].append(decision)
                    if decision.timestamp >= tick_end:
                        for participant in participants:
                            mean_decision_vector = (
                                last_decision[participant.code].decision_vector)
                            if tick_decisions[participant.code]:
                                tick_decision_vectors = [
                                    d.decision_vector
                                    for d in tick_decisions[participant.code]]
                                mean_decision_vector = (
                                    sum(tick_decision_vectors) /
                                    len(tick_decision_vectors))
                            round_ticks.append({
                                'tick': tick,
                                'participant': participant.code,
                                'mean_decision': mean_decision_vector,
                                'session': session.code,
                                'subsession': (
                                    last_decision[participant.code].subsession),
                                'round': roundno,
                                'group': last_decision[participant.code].group
                            })
                        tick_decisions.clear()
                        tick_end += datetime.timedelta(seconds=1)
                        tick += 1
            ticks += round_ticks
        return [
                'tick',
                'session',
                'subsession',
                'round',
                'group',
                'participant',
                'mean_decision'
        ], ticks