from mmobot.db.models import Player

TEST_TOWN_SQUARE_ZONE_ID = 0
TEST_CHANNEL_TOWN_SQUARE_NAME = 'town-square'
TEST_CHANNEL_TOWN_SQUARE_ID = 1057779933675524156

TEST_MARKETPLACE_ZONE_ID = 4
TEST_CHANNEL_MARKETPLACE_NAME = 'marketplace'
TEST_CHANNEL_MARKETPLACE_ID = 1057779938188607630

TEST_PLAYER_ENTITY_NUMBER = 2222
TEST_PLAYER_DISCORD_ID = 100
TEST_PLAYER_DISCORD_NAME = 'player'

TEST_PLAYER_ENTITY_NUMBER_2 = 3333
TEST_PLAYER_DISCORD_ID_2 = 120
TEST_PLAYER_DISCORD_NAME_2 = 'playerTwo'

TEST_PLAYER = Player(
    id=TEST_PLAYER_ENTITY_NUMBER,
    name=TEST_PLAYER_DISCORD_NAME,
    discord_id=TEST_PLAYER_DISCORD_ID,
    is_active=True
)

TEST_ITEM_ENTITY_NUMBER = 200
TEST_ITEM_ENTITY_REFERENCE = '/5k'
TEST_ITEM_ENTITY_NUMBER_2 = 201
TEST_ITEM_ENTITY_REFERENCE_2 = '/5l'
TEST_ITEM_ENTITY_NUMBER_3 = 202
TEST_ITEM_ENTITY_REFERENCE_3 = '/5m'

TEST_IRON_SWORD_WEIGHT = 30
TEST_WOODEN_BOW_WEIGHT = 5

MESSAGE_TEST_PLAYER_INCAPACITATED = '<@100> You are incapacitated.'
