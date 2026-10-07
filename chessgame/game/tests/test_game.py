import json
from django.test import TestCase

class ChessGameTests(TestCase):
    def test_home_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ChessArena')

    def test_new_game_has_starting_position(self):
        self.client.get('/')
        response = self.client.post('/api/new-game/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['turn'], 'white')
        self.assertFalse(response.json()['game_over'])

    def test_legal_player_move_and_ai_response(self):
        self.client.get('/')
        response = self.client.post('/api/move/', data=json.dumps({'uci': 'e2e4'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['player_move'], 'e4')
        self.assertIsNotNone(data['computer_move'])
        self.assertEqual(data['turn'], 'white')

    def test_illegal_move_rejected(self):
        self.client.get('/')
        response = self.client.post('/api/move/', data=json.dumps({'uci': 'e2e5'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_health_endpoint(self):
        response = self.client.get('/api/health/')
        self.assertEqual(response.json()['status'], 'ok')
