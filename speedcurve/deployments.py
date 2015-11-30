from .models import SpeedCurveCore


class Deployment(SpeedCurveCore):
    """Deployment class."""

    def _update_attributes(self, json):
        self.id = json.get('deploy_id')
        self.tests_completed = json.get('tests-completed')
        self.status = json.get('status')
        self.tests_remaining = json.get('tests-remaining')
        self.note = json.get('note')
        self.detail = json.get('detail')

    def __repr__(self):
        return '<Deployment [{}]>'.format(self.id)
