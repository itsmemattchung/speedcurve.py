"""Note Class."""
from .models import SpeedCurveCore


class Note(SpeedCurveCore):
    """SpeedCurve Note Class."""

    def _update_attributes(self, json):
        self.id = json.get('note_id')
        self.site_id = json.get('site_id')
        self.note = json.get('note')
        self.detail = json.get('detail')

    def __repr__(self):
        """Return formatted string of instance."""
        return '<Note [{}]>'.format(self.id)
