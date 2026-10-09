from dataclasses import dataclass
from datetime import datetime, timezone
from flask import Flask, jsonify, send_from_directory

# ========================
# CONFIGURATION
# ========================

@dataclass(frozen=True)
class TokenmobileConfig:
    rack_id: str
    rack_color: str
    start_timestamp: float
    value_increment_per_minute: float
    cycle_durations_seconds: list

    boost_percent: int
    supply_current: int
    supply_total: int








RACKS = {

"tokenmobiles-1": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-1",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        25833600,   # 299 days
        38750400,   # 1 year 83 days 12 hours
        58125600,   # 1 year 307 days 18 hours
        87188400    # 2 years 279 days 3 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#ffc44c"
),

"tokenmobiles-2": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-2",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        8294400,    # 96 days
        9123840,    # 105 days 14 hours 24 minutes
        10036224,   # 116 days 3 hours 50 minutes 24 seconds
        11039846,   # 127 days 18 hours 37 minutes 26 seconds
        12143831,   # 140 days 13 hours 17 minutes 11 seconds
        13358214,   # 154 days 14 hours 36 minutes 54 seconds
        14694036,   # 170 days 1 hour 40 minutes 36 seconds
        16163439,   # 187 days 1 hour 50 minutes 39 seconds
        17779783,   # 205 days 18 hours 49 minutes 43 seconds
        19557761,   # 226 days 8 hours 42 minutes 41 seconds
        21513537,   # 248 days 23 hours 58 minutes 57 seconds
        23664891,   # 273 days 21 hours 34 minutes 51 seconds
        26031380,   # 301 days 6 hours 56 minutes 20 seconds
        28634518,   # 331 days 10 hours 1 minute 58 seconds
        31497970,   # 364 days 13 hours 26 minutes 10 seconds
        34647767    # 1 year 36 days 22 minutes 47 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#00effe"

),

"tokenmobiles-3": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-3",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        11836800,   # 137 days
        14204160,   # 164 days 9 hours 36 minutes
        17044992,   # 197 days 6 hours 43 minutes 12 seconds
        20453990,   # 236 days 17 hours 39 minutes 50 seconds
        24544788,   # 284 days 1 hour 59 minutes 48 seconds
        29453746,   # 340 days 21 hours 35 minutes 46 seconds
        35344495,   # 1 year 44 days 1 hour 54 minutes 55 seconds
        42413394    # 1 year 125 days 21 hours 29 minutes 54 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#a1e6ad"

),

"tokenmobiles-4": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-4",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        13392000,   # 155 days
        16070400,   # 186 days
        19284480,   # 223 days 4 hours 48 minutes
        23141376,   # 267 days 20 hours 9 minutes 36 seconds
        27769651,   # 321 days 9 hours 47 minutes 31 seconds
        33323581,   # 1 year 20 days 16 hours 33 minutes 1 second
        39988298,   # 1 year 97 days 19 hours 51 minutes 38 seconds
        47985957,   # 1 year 190 days 9 hours 25 minutes 57 seconds
        57583149,   # 1 year 301 days 11 hours 19 minutes 9 seconds
        69099778    # 2 years 69 days 18 hours 22 minutes 58 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#999999"
),

"tokenmobiles-5": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-5",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        8553600,    # 99 days
        9408960,    # 108 days 21 hours 36 minutes
        10349856,   # 119 days 18 hours 57 minutes 36 seconds
        11384842,   # 131 days 18 hours 27 minutes 22 seconds
        12523326,   # 144 days 22 hours 42 minutes 6 seconds
        13775658,   # 159 days 10 hours 34 minutes 18 seconds
        15153224,   # 175 days 9 hours 13 minutes 44 seconds
        16668547,   # 192 days 22 hours 9 minutes 7 seconds
        18335401,   # 212 days 5 hours 10 minutes 1 second
        20168941,   # 233 days 10 hours 29 minutes 1 second
        22185836,   # 256 days 18 hours 43 minutes 56 seconds
        24404419,   # 282 days 11 hours 19 seconds
        26844861,   # 310 days 16 hours 54 minutes 21 seconds
        29529347,   # 341 days 18 hours 35 minutes 47 seconds
        32482282,   # 1 year 10 days 22 hours 51 minutes 22 seconds
        35730510,   # 1 year 48 days 13 hours 8 minutes 30 seconds
        39303561    # 1 year 89 days 21 hours 39 minutes 21 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=30000,
    rack_color="#fe0000"
),

"tokenmobiles-6": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-6",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        18748800,     # 217 days
        24373440,     # 282 days 2 hours 24 minutes
        31685472,     # 1 year 1 day 17 hours 31 minutes 12 seconds
        41191114,     # 1 year 111 days 17 hours 58 minutes 34 seconds
        53548448,     # 1 year 254 days 18 hours 34 minutes 8 seconds
        69612982,     # 2 years 75 days 16 hours 56 minutes 22 seconds
        90496877,     # 2 years 317 days 10 hours 1 minute 17 seconds
        117645940,    # 3 years 266 days 15 hours 25 minutes 40 seconds
        152939721,    # 4 years 310 days 3 hours 15 minutes 21 seconds
        198821638,    # 6 years 111 days 4 hours 13 minutes 58 seconds
        258468129,    # 8 years 71 days 12 hours 42 minutes 9 seconds
        336008568,    # 10 years 238 days 23 hours 42 minutes 48 seconds
        436811138,    # 13 years 310 days 16 hours 25 minutes 38 seconds
        567854480     # 18 years 2 days 9 hours 21 minutes 20 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#295fcc"
),

"tokenmobiles-7": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-7",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        13219200,   # 153 days
        14541120,   # 168 days 7 hours 12 minutes
        15995232,   # 185 days 3 hours 7 minutes 12 seconds
        17594755,   # 203 days 15 hours 25 minutes 55 seconds
        19354231,   # 224 days 10 minutes 31 seconds
        21289654,   # 246 days 9 hours 47 minutes 34 seconds
        23418619,   # 271 days 1 hour 10 minutes 19 seconds
        25760481,   # 298 days 3 hours 41 minutes 21 seconds
        28336529,   # 327 days 23 hours 15 minutes 29 seconds
        31170182,   # 360 days 18 hours 23 minutes 2 seconds
        34287200,   # 1 year 31 days 20 hours 13 minutes 20 seconds
        37715920,   # 1 year 71 days 12 hours 38 minutes 40 seconds
        41487512,   # 1 year 115 days 4 hours 18 minutes 32 seconds
        45636264,   # 1 year 163 days 4 hours 44 minutes 24 seconds
        50199890,   # 1 year 216 days 24 minutes 50 seconds
        55219879    # 1 year 274 days 2 hours 51 minutes 19 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=20000,
    rack_color="#ffffff"
),

"tokenmobiles-8": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-8",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        6220800,   # 72 days
        6842880    # 79 days 4 hours 48 minutes
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=999,
    rack_color="#ffffff"
),

"tokenmobiles-9": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-9",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        12960000,   # 150 days
        15552000,   # 180 days
        18662400,   # 216 days
        22394880,   # 259 days 4 hours 48 minutes
        26873856,   # 311 days 57 minutes 36 seconds
        32248627,   # 1 year 8 days 5 hours 57 minutes 7 seconds
        38698353,   # 1 year 82 days 21 hours 32 minutes 33 seconds
        46438023,   # 1 year 172 days 11 hours 27 minutes 3 seconds
        55725628    # 1 year 279 days 23 hours 20 minutes 28 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffffff"
),

"tokenmobiles-10": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-10",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        30672000,    # 355 days
        46008000,    # 1 year 167 days 12 hours
        69012000,    # 2 years 68 days 18 hours
        103518000,   # 3 years 103 days 3 hours
        155277000    # 4 years 337 days 4 hours 30 minutes
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#3796f0"
),

"tokenmobiles-11": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-11",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        10022400,   # 116 days
        12026880,   # 139 days 4 hours 48 minutes
        14432256,   # 167 days 57 minutes 36 seconds
        17318707,   # 200 days 10 hours 45 minutes 7 seconds
        20782449,   # 240 days 12 hours 54 minutes 9 seconds
        24938938,   # 288 days 15 hours 28 minutes 58 seconds
        29926726,   # 346 days 8 hours 58 minutes 46 seconds
        35912071    # 1 year 50 days 15 hours 34 minutes 31 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#feee99"
),

"tokenmobiles-12": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-12",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        18057600,    # 209 days
        27086400,    # 313 days 12 hours
        40629600,    # 1 year 105 days 6 hours
        60944400,    # 1 year 340 days 9 hours
        91416600,    # 2 years 328 days 1 hour 30 minutes
        137124900,   # 4 years 127 days 2 hours 15 minutes
        205687350,   # 6 years 190 days 15 hours 22 minutes 30 seconds
        308531025    # 9 years 285 days 23 hours 3 minutes 45 seconds
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=500,
    rack_color="#cccccc"
),

"tokenmobiles-13": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-13",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        21340800,    # 247 days
        27743040,    # 321 days 2 hours 24 minutes
        36065952,    # 1 year 52 days 10 hours 19 minutes 12 seconds
        46885738,    # 1 year 177 days 15 hours 48 minutes 58 seconds
        60951459,    # 1 year 340 days 10 hpurs 57 minutes 39 seconds
        79236897,    # 2 years 187 days 2 hours 14 minutes 57 seconds
        103007966,   # 3 years 97 days 5 hours 19 minutes 26 seconds
        133910355,   # 4 years 89 days 21 hours 19 minutes 15 seconds
        174083462,   # 5 years 189 days 20 hours 31 minutes 2 seconds
        226308500,   # 7 years 64 days 7 hours 28 minutes 20 seconds
        294201050,   # 9 years 120 days 2 hours 30 minutes 50 seconds
        382461365,   # 12 years 46 days 15 hours 16 minutes 5 seconds
        497199775    # 15 years 279 days 15 hours 2 minutes 55 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#00f400"
),

"tokenmobiles-14": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-14",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        15984000,   # 185 days
        19180800,   # 222 days
        23016960,   # 266 days 9 hours 36 minutes
        27620352,   # 319 days 16 hours 19 minutes 12 seconds
        33144422,   # 1 year 18 days 14 hours 47 minutes 2 seconds
        39773307,   # 1 year 95 days 8 hours 8 minutes 27 seconds
        47727968,   # 1 year 187 days 9 hours 46 minutes 8 seconds
        57273562    # 1 year 297 days 21 hours 19 minutes 22 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=30000,
    rack_color="#ffffff"
),

"tokenmobiles-15": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-15",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        21859200,    # 253 days
        32788800,    # 1 year 14 days 12 hours
        49183200,    # 1 year 204 days 6 hours
        73774800,    # 2 years 123 days 21 hours
        110662200,   # 3 years 185 days 19 hours 30 minutes
        165993300    # 5 years 96 days 5 hours 15 minutes
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#fe0000"
),

"tokenmobiles-16": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-16",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        17193600,    # 199 days
        22351680,    # 258 days 16 hours 48 minutes
        29057184,    # 336 days 7 hours 26 minutes 24 seconds
        37774339,    # 1 year 72 days 4 hours 52 minutes 19 seconds
        49106641,    # 1 year 203 days 8 hours 44 minutes 1 second
        63838633,    # 2 years 8 days 20 hours 57 minutes 13 seconds
        82990223,    # 2 years 230 days 12 hours 50 minutes 23 seconds
        107887290,   # 3 years 153 days 16 hours 41 minutes 30 seconds
        140253477,   # 4 years 163 days 7 hours 17 minutes 57 seconds
        182329520,   # 5 years 285 days 7 hours 5 minutes 20 seconds
        237028377,   # 7 years 188 days 9 hours 12 minutes 57 seconds
        308136890    # 9 years 281 days 9 hours 34 minutes 50 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#ffffff"
),

"tokenmobiles-17": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-17",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        14428800,   # 167 days
        17314560,   # 200 days 9 hours 36 minutes
        20777472,   # 240 days 11 hours 31 minutes 12 seconds
        24932966,   # 288 days 13 hours 49 minutes 26 seconds
        29919560,   # 346 days 6 hours 59 minutes 20 seconds
        35903472,   # 1 year 50 days 13 hours 11 minutes 12 seconds
        43084166,   # 1 year 133 days 15 hours 49 minutes 26 seconds
        51700999,   # 1 year 233 days 9 hours 23 minutes 19 seconds
        62041199,   # 1 year 353 days 1 hour 39 minutes 59 seconds
        74449439    # 2 years 131 days 16 hours 23 minutes 59 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#ffcb99"
),

"tokenmobiles-18": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-18",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        21513600,    # 249 days
        30119040,    # 348 days 14 hours 24 minutes
        42166656,    # 1 year 123 days 57 minutes 36 seconds
        59033318,    # 1 year 318 days 6 hours 8 minutes 38 seconds
        82646646,    # 2 years 226 days 13 hours 24 minutes 6 seconds
        115705304,   # 3 years 244 days 4 hours 21 minutes 44 seconds
        161987426,   # 5 years 49 days 20 hours 30 minutes 26 seconds
        226782396,   # 7 years 69 days 19 hours 6 minutes 36 seconds
        317495354,   # 10 years 24 days 17 hours 9 minutes 14 seconds
        444493496    # 14 years 34 days 14 hours 24 minutes 56 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=5000,
    rack_color="#ffffff"
),

"tokenmobiles-19": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-19",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16416000,   # 190 days
        19699200,   # 228 days
        23639040,   # 273 days 14 hours 24 minutes
        28366848,   # 328 days 7 hours 40 minutes 48 seconds
        34040218,   # 1 year 28 days 23 hours 36 minutes 58 seconds
        40848261,   # 1 year 107 days 18 hours 44 minutes 21 seconds
        49017913,   # 1 year 202 days 8 hours 5 minutes 13 seconds
        58821496,   # 1 year 315 days 19 hours 18 minutes 16 seconds
        70585795    # 2 years 86 days 23 hours 9 minutes 55 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#d1076a"
),

"tokenmobiles-20": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-20",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        21600000,    # 299 days
        30240000,    # 350 days
        42336000,    # 1 year 125 days
        59270400,    # 1 year 321 days
        82978560,    # 2 years 230 days 9 hours 36 minutes
        116169984,   # 3 years 249 days 13 hours 26 minutes 24 seconds
        162637978,   # 5 years 57 days 9 hours 12 minutes 58 seconds
        227693169,   # 7 years 80 days 8 hours 6 minutes 9 seconds
        318770436    # 10 years 39 days 11 hours 20 minutes 36 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=5000,
    rack_color="#ffffff"
),

"tokenmobiles-21": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-21",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16070400,   # 186 days
        19284480,   # 223 days 4 hours 48 minutes
        23141376,   # 267 days 20 hours 9 minutes 36 seconds
        27769651,   # 321 days 9 hours 47 minutes 31 seconds
        33323581,   # 1 year 20 days 16 hours 33 minutes 1 second
        39988298,   # 1 year 97 days 19 hours 51 minutes 38 seconds
        47985957,   # 1 year 190 days 9 hours 25 minutes 57 seconds
        57583149,   # 1 year 301 days 11 hours 19 minutes 9 seconds
        69099778,   # 2 years 69 days 18 hours 22 minutes 58 seconds
        82919734,   # 2 years 229 days 17 hours 15 minutes 34 seconds
        99503681    # 3 years 56 days 15 hours 54 minutes 41 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=1000,
    rack_color="#009999"
),

"tokenmobiles-22": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-22",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16934400,    # 196 days
        22014720,    # 254 days 19 hours 12 minutes
        28619136,    # 331 days 5 hours 45 minutes 36 seconds
        37204877,    # 1 year 65 days 14 hours 41 minutes 17 seconds
        48366340,    # 1 year 194 days 19 hours 5 minutes 40 seconds
        62876242,    # 1 year 362 days 17 hours 37 minutes 22 seconds
        81739114,    # 2 years 216 days 1 hour 18 minutes 34 seconds
        106260849,   # 3 years 134 days 20 hours 54 minutes 9 seconds
        138139103,   # 4 years 138 days 19 hours 58 minutes 23 seconds
        179580834,   # 5 years 253 days 11 hours 33 minutes 54 seconds
        233455084,   # 7 years 147 days 38 minutes 4 seconds
        303491610,   # 9 years 227 days 15 hours 13 minutes 30 seconds
        394539093    # 12 years 186 days 10 hours 11 minutes 33 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#01a60c"
),

"tokenmobiles-23": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-23",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        15120000,   # 175 days
        16632000,   # 192 days 12 hours
        18295200,   # 211 days 18 hours
        20124720,   # 232 days 22 hours 12 minutes
        22137192,   # 256 days 5 hours 13 minutes 12 seconds
        24350911,   # 281 days 20 hours 8 minutes 31 seconds
        26786002,   # 310 days 33 minutes 22 seconds
        29464603    # 341 days 36 minutes 43 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=20000,
    rack_color="#cccccc"
),

"tokenmobiles-24": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-24",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        20649600,    # 239 days
        28909440,    # 334 days 14 hours 24 minutes
        40473216,    # 1 year 103 days 10 hours 33 minutes 36 seconds
        56662502,    # 1 year 290 days 19 hours 35 minutes 2 seconds
        79327503,    # 2 years 188 days 3 hours 25 minutes 3 seconds
        111058505,   # 3 years 190 days 9 hours 35 minutes 5 seconds
        155481907,   # 4 years 339 days 13 hours 25 minutes 7 seconds
        217674669,   # 6 years 329 days 9 hours 11 minutes 9 seconds
        304744537    # 9 years 242 days 3 hours 15 minutes 37 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=10000,
    rack_color="#cccccc"
),

"tokenmobiles-25": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-25",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        20304000,    # 235 days
        28425600,    # 329 days
        39795840,    # 1 year 95 days 14 hours 24 minutes
        55714176,    # 1 year 279 days 20 hours 9 minutes 36 seconds
        77999846,    # 2 years 172 days 18 hours 37 minutes 26 seconds
        109199785,   # 3 years 168 days 21 hours 16 minutes 25 seconds
        152879699,   # 4 years 309 days 10 hours 34 minutes 59 seconds
        214031579,   # 6 years 287 days 5 hours 12 minutes 59 seconds
        299644210    # 9 years 183 days 2 hours 30 minutes 10 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=20000,
    rack_color="#f53041"
),

"tokenmobiles-26": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-26",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        21254400,   # 246 days
        27630720,   # 319 days 19 hours 12 minutes
        35919936,   # 1 year 50 days 17 hours 45 minutes 36 seconds
        46695917,   # 1 year 175 days 11 hours 5 minutes 17 seconds
        60704691,   # 1 year 337 days 14 hours 24 minutes 51 seconds
        78916099,   # 2 years 183 days 9 hours 8 minutes 19 seconds
        102590929   # 3 years 92 days 9 hours 28 minutes 49 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=1000,
    rack_color="#295fcc"
),

"tokenmobiles-27": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-27",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        22809600,    # 264 days
        34214400,    # 1 year 31 days
        51321600,    # 1 year 229 days
        76982400,    # 2 years 161 days
        115473600,   # 3 years 241 days 12 hours
        173210400    # 5 years 179 days 18 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=5000,
    rack_color="#ffffff"
),

"tokenmobiles-28": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-28",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        17712000,   # 205 days
        21254400,   # 246 days
        25505280,   # 295 days 4 hours 48 minutes
        30606336,   # 354 days 5 hours 45 minutes 36 seconds
        36727603,   # 1 year 60 days 2 hours 6 minutes 43 seconds
        44073124,   # 1 year 145 days 2 hours 32 minutes 4 seconds
        52887749,   # 1 year 247 days 3 hours 2 minutes 29 seconds
        63465298,   # 2 years 4 days 13 hours 14 minutes 58 seconds
        76158358,   # 2 years 151 days 11 hours 5 minutes 58 seconds
        91390030    # 2 years 327 days 18 hours 7 minutes 10 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#73e7e6"
),

"tokenmobiles-29": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-29",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        12614400,   # 146 days
        13875840,   # 160 days 14 hours 24 minutes
        15263424,   # 176 days 15 hours 50 minutes 24 seconds
        16789766,   # 194 days 7 hours 49 minutes 26 seconds
        18468743,   # 213 days 18 hours 12 minutes 23 seconds
        20315617,   # 235 days 3 hours 13 minutes 37 seconds
        22347179,   # 258 days 15 hours 32 minutes 59 seconds
        24581897,   # 284 days 12 hours 18 minutes 17 seconds
        27040087,   # 312 days 23 hours 8 minutes 7 seconds
        29744095,   # 344 days 6 hours 14 minutes 55 seconds
        32718505,   # 1 year 13 days 16 hours 28 minutes 25 seconds
        35990355,   # 1 year 51 days 13 hours 19 minutes 15 seconds
        39589391,   # 1 year 93 days 5 hours 3 minutes 11 seconds
        43548330,   # 1 year 139 days 45 minutes 30 seconds
        47903163,   # 1 year 189 days 10 hours 26 minutes 3 seconds
        52693479,   # 1 year 244 days 21 hours 4 minutes 39 seconds
        57962827    # 1 year 305 days 20 hours 47 minutes 7 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffe459"
),

"tokenmobiles-30": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-30",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        29289600,   # 339 days
        43934400,   # 1 year 143 days 12 hours
        65901600,   # 2 years 32 days 18 hours
        98852400,   # 3 years 49 days 3 hours
        148278600,  # 4 years 256 days 4 hours 30 minutes
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#cccccc"
),

"tokenmobiles-31": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-31",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        21600000,   # 250 days
        25920000,   # 300 days
        31104000,   # 360 days
        37324800,   # 1 year 67 days
        44789760,   # 1 year 153 days 9 hours 36 minutes
        53747712,   # 1 year 257 days 1 hour 55 minutes 12 seconds
        64497254,   # 2 years 16 days 11 hours 54 minutes 14 seconds
        77396705,   # 2 years 165 days 19 hours 5 minutes 5 seconds
        92876046    # 2 years 344 days 22 hours 54 minutes 6 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#ffffff"
),

"tokenmobiles-32": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-32",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        25747200,   # 298 days
        38620800,   # 1 year 82 days
        57931200,   # 1 year 305 days 12 hours
        86896800    # 2 years 275 days 18 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#cccccc"
),

"tokenmobiles-33": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-33",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16934400,    # 196 days
        22014720,    # 254 days 19 hours 12 minutes
        28619136,    # 331 days 5 hours 45 minutes 36 seconds
        37204877,    # 1 year 65 days 14 hours 41 minutes 17 seconds
        48366340,    # 1 year 194 days 19 hours 5 minutes 40 seconds
        62876242,    # 1 year 362 days 17 hours 37 minutes 22 seconds
        81739114,    # 2 years 216 days 1 hour 18 minutes 34 seconds
        106260849,   # 3 years 134 days 20 hours 54 minutes 9 seconds
        138139103    # 4 years 138 days 19 hours 58 minutes 23 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#da0092"
),

"tokenmobiles-34": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-34",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16675200,   # 193 days
        18342720,   # 212 days 7 hours 12 minutes
        20176992,   # 233 days 12 hours 43 minutes 12 seconds
        22194691,   # 256 days 21 hours 11 minutes 31 seconds
        24414160,   # 282 days 13 hours 42 minutes 40 seconds
        26855576,   # 310 days 19 hours 52 minutes 56 seconds
        29541134,   # 341 days 21 hours 52 minutes 14 seconds
        32495247,   # 1 year 11 days 2 hours 27 minutes 27 seconds
        35744772,   # 1 year 48 days 17 hours 6 minutes 12 seconds
        39319249,   # 1 year 90 days 2 hours 49 seconds
        43251174    # 1 year 135 days 14 hours 12 minutes 54 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffffff"
),

"tokenmobiles-35": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-35",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        21427200,    # 248 days
        29998080,    # 347 days 4 hours 48 minutes
        41997312,    # 1 year 121 days 1 hour 55 minutes 12 seconds
        58796237,    # 1 year 315 days 12 hours 17 minutes 17 seconds
        82314732,    # 2 years 222 days 17 hours 12 minutes 12 seconds
        115240624,   # 3 years 238 days 19 hours 17 minutes 4 seconds
        161336874,   # 5 years 42 days 7 hours 47 minutes 54 seconds
        225871623    # 7 years 59 days 6 hours 7 minutes 3 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffffff"
),

"tokenmobiles-36": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-36",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        20390400,    # 236 days
        26507520,    # 306 days 19 hours 12 minutes
        34459776,    # 1 year 33 days 20 hours 9 minutes 36 seconds
        44797709,    # 1 year 153 days 11 hours 48 minutes 29 seconds
        58237021,    # 1 year 309 days 57 minutes 1 second
        75708128,    # 2 years 146 days 6 hours 2 minutes 8 seconds
        98420566,    # 3 years 44 days 3 hours 2 minutes 46 seconds
        127946736,   # 4 years 20 days 20 hours 45 minutes 36 secons
        166330757,   # 5 years 100 days 2 hours 59 minutes 17 seconds
        216229984,   # 6 years 312 days 15 hours 53 minutes 4 seconds
        281098979,   # 8 years 333 days 11 hours 2 minutes 59 seconds
        365428673,   # 11 years 214 days 11 hours 57 minutes 53 seconds
        475057275,   # 15 years 23 days 8 hours 21 minutes 15 seconds
        617574457    # 19 years 212 days 20 hours 27 minutes 37 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#ff7300"
),

"tokenmobiles-37": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-37",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16848000,    # 195 days
        23587200,    # 273 days
        33022080,    # 1 year 17 days 4 hours 48 minutes
        46230912,    # 1 year 170 days 1 hour 55 minutes 12 seconds
        64723277,    # 2 years 19 days 2 hours 41 minutes 17 seconds
        90612588,    # 2 years 318 days 18 hours 9 minutes 48 seconds
        126857623,   # 4 years 8 days 6 hours 13 minutes 43 seconds
        177600672,   # 5 years 230 days 13 hours 31 minutes 12 seconds
        248640940    # 7 years 322 days 18 hours 55 minutes 40 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=5000,
    rack_color="#cccccc"
),

"tokenmobiles-38": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-38",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        10540800,   # 122 days
        11594880,   # 134 days 4 hours 48 minutes
        12754368    # 147 days 14 hours 52 minutes 48 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffffff"
),

"tokenmobiles-39": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-39",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        7603200,   # 88 days
        8363520    # 96 days 19 hours 12 minutes
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=30000,
    rack_color="#ffd300"
),

"tokenmobiles-40": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-40",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        27993600,    # 324 days
        41990400,    # 1 year 121 days
        62985600,    # 1 year 364 days
        94478400,    # 2 years 363 days 12 hours
        141717600    # 4 years 180 days 6 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#fe0000"
),

"tokenmobiles-41": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-41",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        15033600,   # 174 days
        18040320,   # 208 days 19 hours 12 minutes
        21648384,   # 250 days 13 hours 26 minutes 24 seconds
        25978061,   # 300 days 16 hours 7 minutes 41 seconds
        31173673,   # 360 days 19 hours 21 minutes 13 seconds
        37408408,   # 1 year 67 days 23 hours 13 minutes 28 seconds
        44890089,   # 1 year 154 days 13 hours 28 minutes 9 seconds
        53868107,   # 1 year 258 days 11 hours 21 minutes 47 seconds
        64641728,   # 2 years 18 days 4 hours 2 minutes 8 seconds
        77570074    # 2 years 167 days 19 hours 14 minutes 34 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=30000,
    rack_color="#cccccc"
),

"tokenmobiles-42": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-42",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        22636800,   # 262 days
        27164160,   # 314 days 9 hours 36 minutes
        32596992,   # 1 year 12 days 6 hours 43 minutes 12 seocnds
        39116390,   # 1 year 87 days 17 hours 39 minutes 50 seconds
        46939668,   # 1 year 178 days 6 hours 47 minutes 48 seconds
        56327602,   # 1 year 286 days 22 hours 33 minutes 22 seconds
        67593123,   # 2 years 52 days 7 hours 52 minutes 3 seconds
        81111747,   # 2 years 208 days 19 hours 2 minutes 27 seconds
        97334097    # 3 years 31 days 13 hours 14 minutes 57 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#2020fe"
),

"tokenmobiles-43": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-43",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        25660800,     # 297 days
        35925120,     # 1 year 50 days 19 hours 12 minutes
        50295168,     # 1 year 217 days 2 hours 52 minutes 48 seconds
        70413235,     # 2 years 84 days 23 hours 13 minutes 55 seconds
        98578529,     # 3 years 45 days 22 hours 55 minutes 29 seconds
        138009941,    # 4 years 137 days 8 hours 5 minutes 41 seconds
        193213917,    # 6 years 46 days 6 hours 31 minutes 57 seconds
        270499484,    # 8 years 210 days 18 hours 44 minutes 44 seconds
        378699278,    # 12 years 3 days 2 hours 14 minutes 38 seconds
        530178989,    # 16 years 296 days 7 hours 56 minutes 29 seconds
        742250585,    # 23 years 195 days 20 hours 43 minutes 5 seconds
        1039150819,   # 32 years 347 days 5 hours 19 seconds
        1454811147,   # 46 years 48 days 2 hours 12 minutes 27 seconds
        2036735605    # 64 years 213 days 7 hours 53 minutes 25 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=200,
    rack_color="#3796f0"
),

"tokenmobiles-44": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-44",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        18144000,    # 210 days
        21772800,    # 252 days
        26127360,    # 302 days 9 hours 36 minutes
        31352832,    # 362 days 21 hours 7 minutes 12 seconds
        37623398,    # 1 year 70 days 10 hours 56 minutes 38 seconds
        45148078,    # 1 year 157 days 13 hours 7 minutes 58 seconds
        54177694,    # 1 year 262 days 1 hour 21 minutes 34 seconds
        65013232,    # 2 years 22 days 11 hours 13 minutes 52 seconds
        78015879,    # 2 years 172 days 23 hours 4 minutes 39 seconds
        93619055,    # 2 years 353 days 13 hours 17 minutes 35 seconds
        112342866,   # 3 years 205 days 6 hours 21 minutes 6 seconds
        134811439,   # 4 years 100 days 7 hours 37 minutes 19 seconds
        161773727,   # 5 years 47 days 9 hours 8 minutes 47 seconds
        194128472,   # 6 years 56 days 20 hours 34 minutes 32 seconds
        232954166,   # 7 years 141 days 5 hours 29 minutes 26 seconds
        279544999,   # 8 years 315 days 11 hours 23 minutes 19 seconds
        335453999,   # 10 years 232 days 13 hours 39 minutes 59 seconds
        402544799,   # 12 years 279 days 1 hour 59 minutes 59 seconds
        483053759,   # 15 years 115 days 21 hours 35 minutes 59 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=1000,
    rack_color="#ffffff"
),

"tokenmobiles-45": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-45",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        19699200,    # 228 days
        29548800,    # 342 days
        44323200,    # 1 year 148 days
        66484800,    # 2 years 39 days 12 hours
        99727200,    # 3 years 59 days 6 hours
        149590800    # 4 years 271 days 9 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#cccccc"
),

"tokenmobiles-46": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-46",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        12441600,   # 144 days
        14929920,   # 172 days 19 hours 12 minutes
        17915904,   # 207 days 8 hours 38 minutes 24 seconds
        21499085,   # 248 days 19 hours 58 minutes 5 seconds
        25798902,   # 298 days 14 hours 21 minutes 42 seconds
        30958682,   # 358 days 7 hours 38 minutes 2 seconds
        37150419,   # 1 year 64 days 23 hours 33 minutes 39 seconds
        44580502    # 1 year 150 days 23 hours 28 minutes 22 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#ee4957"
),

"tokenmobiles-47": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-47",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        19180800,   # 222 days
        28771200,   # 333 days
        43156800,   # 1 year 134 days 12 hours
        64735200    # 2 years 19 days 6 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#ffffff"
),

"tokenmobiles-48": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-48",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        13478400,   # 156 days
        14826240,   # 171 days 14 hours 24 minutes
        16308864,   # 188 days 18 hours 14 minutes 24 seconds
        17939750,   # 207 days 15 hours 15 minutes 50 seconds
        19733725,   # 228 days 9 hours 35 minutes 25 seconds
        21707098,   # 251 days 5 hours 44 minutes 58 seconds
        23877808,   # 276 days 8 hours 43 minutes 28 seconds
        26265589,   # 303 days 23 hours 59 minutes 49 seconds
        28892147,   # 334 days 9 hours 35 minutes 47 seconds
        31781362,   # 1 year 2 days 20 hours 9 minutes 22 seconds
        34959498    # 1 year 39 days 14 hours 58 minutes 18 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#feee99"
),

"tokenmobiles-49": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-49",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        18144000,   # 210 days
        19958400,   # 231 days
        21954240,   # 254 days 2 hours 24 minutes
        24149664,   # 279 days 12 hours 14 minutes 24 seconds
        26564630,   # 307 days 11 hours 3 minutes 50 seconds
        29221093,   # 338 days 4 hours 58 minutes 13 seconds
        32143203,   # 1 year 7 days 40 minutes 3 seconds
        35357523,   # 1 year 44 days 5 hours 32 minutes 3 seconds
        38893275,   # 1 year 85 days 3 hours 41 minutes 15 seconds
        42782603,   # 1 year 130 days 4 hours 3 minues 23 seconds
        47060863,   # 1 year 179 days 16 hours 27 minutes 43 seconds
        51766950,   # 1 year 234 days 3 hours 42 minutes 30 seconds
        56943644,   # 1 year 294 days 1 hour 40 minutes 44 seconds
        62638009,   # 1 year 359 days 23 hours 26 minutes 49 seconds
        68901810,   # 2 years 67 days 11 hours 23 minutes 30 seconds
        75791991,   # 2 years 147 days 5 hours 19 minutes 51 seconds
        83371190    # 2 years 234 days 22 hours 39 minutes 50 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=20000,
    rack_color="#cccccc"
),

"tokenmobiles-50": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-50",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        15033600,   # 174 days
        18040320,   # 208 days 19 hours 12 minutes
        21648384,   # 250 days 13 hours 26 minutes 24 seconds
        25978061,   # 300 days 16 hours 7 minutes 41 seconds
        31173673,   # 360 days 19 hours 21 minutes 13 seconds
        37408408,   # 1 year 67 days 23 hours 13 minutes 28 seconds
        44890089,   # 1 year 154 days 13 hours 28 minutes 9 seconds
        53868107,   # 1 year 258 days 11 hours 21 minutes 47 seconds
        64641728,   # 2 years 18 days 4 hours 2 minutes 8 seconds
        77570074,   # 2 years 167 days 19 hours 14 minutes 34 seconds
        93084089,   # 2 years 347 days 8 hours 41 minutes 29 seconds
        111700906   # 3 years 197 days 20 hours 1 minute 46 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=5000,
    rack_color="#73e7e6"
),

"tokenmobiles-51": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-51",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        33350400,    # 1 year 21 days
        50025600,    # 1 year 214 days
        75038400,    # 2 years 138 days 12 hours
        112557600,   # 3 years 207 days 18 hours
        168836400    # 5 years 129 days 3 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#fc8d33"
),

"tokenmobiles-52": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-52",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        15552000,   # 180 days
        18662400,   # 216 days
        22394880,   # 259 days 4 hours 48 minutes
        26873856,   # 311 days 57 minutes 36 seconds
        32248627,   # 1 year 8 days 5 hours 57 minutes 7 seconds
        38698353,   # 1 year 82 days 21 hours 32 minutes 33 seconds
        46438023,   # 1 year 172 days 11 hours 27 minutes 3 seconds
        55725628,   # 1 year 279 days 23 hours 20 minutes 28 seconds
        66870753,   # 2 years 43 days 23 hours 12 minutes 33 seconds
        80244904    # 2 years 198 days 18 hours 15 minutes 4 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffa6ac"
),

"tokenmobiles-53": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-53",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        8380800,   # 97 days
        9218880,   # 106 days 16 hours 48 minutes
        10140768   # 117 days 8 hours 52 minutes 48 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=1000,
    rack_color="#ffffff"
),

"tokenmobiles-54": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-54",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        17366400,    # 201 days
        22576320,    # 261 days 7 hours 12 minutes
        29349216,    # 339 days 16 hours 33 minutes 36 seconds
        38153981,    # 1 year 76 days 14 hours 19 minutes 41 seconds
        49600175,    # 1 year 209 days 1 hour 49 minutes 35 seconds
        64480228,    # 2 years 16 days 7 hours 10 minutes 28 seconds
        83824296,    # 2 years 240 days 4 hours 31 minutes 36 seconds
        108971585,   # 3 years 166 days 5 hours 53 minutes 5 seconds
        141663060,   # 4 years 179 days 14 hours 50 minutes 60 seconds
        184161978,   # 5 yaers 306 days 12 hours 6 minutes 18 seconds
        239410571    # 7 years 215 days 22 hours 56 minutes 11 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#ffff00"
),

"tokenmobiles-55": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-55",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        22723200,    # 263 days
        34084800,    # 1 year 29 days 12 hours
        51127200,    # 1 year 226 days 18 hours
        76690800,    # 2 years 157 days 15 hours
        115036200,   # 3 years 236 days 10 hours 30 minutes
        172554300    # 5 years 172 days 3 hours 45 minutes
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#cccccc"
),

"tokenmobiles-56": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-56",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        20217600,    # 234 days
        26282880,    # 304 days 4 hours 48 minutes
        34167744,    # 1 year 30 days 11 hours 2 minutes 24 seconds
        44418067,    # 1 year 149 days 2 hours 21 minutes 7 seconds
        57743487,    # 1 year 303 days 7 hours 51 minutes 27 seconds
        75066534,    # 2 years 138 days 19 hours 48 minutes 54 seconds
        97586494,    # 3 years 34 days 11 hours 21 minutes 34 seconds
        126862442,   # 4 years 8 days 7 hours 34 minutes 2 seconds
        164921174,   # 5 years 83 days 19 hours 26 minutes 14 seconds
        214397527,   # 6 years 291 days 10 hours 52 minutes 7 seconds
        278716784,   # 8 years 305 days 21 hours 19 minutes 44 seconds
        362331820,   # 11 years 178 days 15 hours 43 minutes 40 seconds
        471031366    # 14 years 341 days 18 hours 2 minutes 46 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#47cc4f"
),

"tokenmobiles-57": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-57",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        11059200,   # 128 days
        12165120,   # 140 days 19 hours 12 minutes
        13381632,   # 154 days 21 hours 7 minutes 12 seconds
        14719795,   # 170 days 8 hours 49 minutes 55 seconds
        16191775,   # 187 days 9 hours 42 minutes 55 seconds
        17810952,   # 206 days 3 hours 29 minutes 12 seconds
        19592047,   # 226 days 18 hours 14 minutes 7 seconds
        21551252,   # 249 days 10 hours 27 minutes 32 seconds
        23706377,   # 274 days 9 hours 6 minutes 17 seconds
        26077015,   # 301 days 19 hours 36 minutes 55 seconds
        28684717,   # 331 days 23 hours 58 minutes 37 seconds
        31553188,   # 1 year 4 hours 46 minutes 28 seconds
        34708507,   # 1 year 36 days 17 hours 15 minutes 7 seconds
        38179358,   # 1 year 76 days 21 hours 22 minutes 38 seconds
        41997294,   # 1 year 121 days 1 hour 54 minutes 54 seconds
        46197023,   # 1 year 169 days 16 hours 30 minutes 23 seconds
        50816725,   # 1 year 223 days 3 hours 45 minutes 25 seconds
        55898398    # 1 year 281 days 23 hours 19 minutes 58 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=20000,
    rack_color="#96b301"
),

"tokenmobiles-58": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-58",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        13824000,   # 160 days
        16588800,   # 192 days
        19906560,   # 230 days 9 hours 36 minutes
        23887872,   # 276 days 11 hours 31 minutes 12 seconds
        28665446,   # 331 days 18 hours 37 minutes 26 seconds
        34398536,   # 1 year 33 days 3 hours 8 minutes 56 seconds
        41278243,   # 1 year 112 days 18 hours 10 minutes 43 seconds
        49533891,   # 1 year 208 days 7 hours 24 minutes 51 seconds
        59440670    # 1 year 322 days 23 hours 17 minutes 50 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffffff"
),

"tokenmobiles-59": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-59",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        18576000,    # 215 days
        26006400,    # 301 days
        36408960,    # 1 year 56 days 9 hours 36 minutes
        50972544,    # 1 year 224 days 23 hours 2 minutes 24 seconds
        71361562,    # 2 years 95 days 22 hours 39 minutes 22 seconds
        99906186,    # 3 years 61 days 7 hours 43 minutes 6 seconds
        139868661,   # 4 years 158 days 20 hours 24 minutes 21 seconds
        195816125    # 6 years 76 days 9 hours 22 minutes 5 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=10000,
    rack_color="#2020fe"
),

"tokenmobiles-60": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-60",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        20736000,    # 240 days
        31104000,    # 360 days
        46656000,    # 1 year 175 days
        69984000,    # 2 years 80 days
        104976000,   # 3 years 120 days
        157464000    # 4 yaers 362 days 12 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#cccccc"
),

"tokenmobiles-61": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-61",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        18748800,   # 217 days
        28123200,   # 325 days 12 hours
        42184800,   # 1 year 123 days 6 hours
        63277200,   # 2 years 2 days 9 hours
        94915800    # 3 years 3 days 13 hours 30 minutes
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#ffffff"
),

"tokenmobiles-62": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-62",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        12096000,   # 140 days
        14515200,   # 168 days
        17418240,   # 201 days 14 hours 24 minutes
        20901888,   # 241 days 22 hours 4 minutes 48 seconds
        25082266,   # 290 days 7 hours 17 minutes 46 seconds
        30098719,   # 348 days 8 hours 45 minutes 19 seconds
        36118462,   # 1 year 53 days 54 minutes 22 seconds
        43342155    # 1 year 136 days 15 hours 29 minutes 15 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#e6c37f"
),

"tokenmobiles-63": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-63",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        18144000,   # 210 days
        21772800,   # 252 days
        26127360,   # 302 days 9 hours 36 minutes
        31352832,   # 362 days 21 hours 7 minutes 12 seconds
        37623398,   # 1 year 70 days 10 hours 56 minutes 38 seconds
        45148078,   # 1 year 157 days 13 hours 7 minutes 58 seconds
        54177694,   # 1 year 262 days 1 hour 21 minutes 34 seconds
        65013232    # 2 years 22 days 11 hours 13 minutes 52 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#ffffff"
),

"tokenmobiles-64": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-64",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        15292800,    # 177 days
        19880640,    # 230 days 2 hours 24 minutes
        25844832,    # 299 days 3 hours 7 minutes 12 seconds
        33598282,    # 1 year 23 days 20 hours 51 minutes 22 seconds
        43677766,    # 1 year 140 days 12 hours 42 minutes 46 seconds
        56781096,    # 1 year 292 days 4 hours 31 minutes 36 seconds
        73815425,    # 2 years 124 days 8 hours 17 minutes 5 seconds
        95960052,    # 3 years 15 days 15 hours 34 minutes 12 seconds
        124748068,   # 3 years 348 days 20 hours 14 minutes 28 seconds
        162172488,   # 5 years 51 days 23 hours 54 minutes 48 seconds
        210824234,   # 6 years 250 days 2 hours 17 minutes 14 seconds
        274071505,   # 8 years 252 days 2 hours 58 minutes 25 seconds
        356292956,   # 11 years 108 days 18 hours 15 minutes 56 seconds
        463180843    # 14 years 250 days 21 hours 20 minutes 43 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#ffffff"
),

"tokenmobiles-65": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-65",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        22204800,   # 257 days
        33307200,   # 1 year 20 days 12 hours
        49960800,   # 1 year 213 days 6 hours
        74941200,   # 2 years 137 days 9 hours
        112411800   # 3 years 206 days 1 hour 30 minutes
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#f53041"
),

"tokenmobiles-66": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-66",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        17193600,   # 199 days
        20632320,   # 238 days 19 hours 12 minutes
        24758784,   # 286 days 13 hours 26 minutes 24 seconds
        29710541,   # 343 days 20 hours 55 minutes 41 seconds
        35652649,   # 1 year 47 days 15 hours 30 minutes 49 seconds
        42783179,   # 1 year 130 days 4 hours 12 minutes 59 seconds
        51339815,   # 1 yaer 229 days 5 hours 3 minutes 35 seconds
        61607777,   # 1 year 348 days 1 hour 16 minutes 17 seconds
        73929333,   # 2 years 125 days 15 hours 55 minutes 33 seconds
        88715199    # 2 years 296 days 19 hours 6 minutes 39 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffa6ac"
),

"tokenmobiles-67": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-67",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        12096000,   # 140 days
        14515200,   # 168 days
        17418240,   # 201 days 14 hours 24 minutes
        20901888,   # 241 days 22 hours 4 minutes 48 seconds
        25082266,   # 290 days 7 hours 17 minutes 46 seconds
        30098719,   # 348 days 8 hours 45 minutes 19 seconds
        36118462,   # 1 year 53 days 54 minutes 22 seconds
        43342155,   # 1 year 136 days 15 hours 29 minutes 15 seconds
        52010586    # 1 year 236 days 23 hours 23 minutes 6 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffe459"
),

"tokenmobiles-68": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-68",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        18748800,   # 217 days
        22498560,   # 260 days 9 hours 36 minutes
        26998272,   # 312 days 11 hours 31 minutes 12 seconds
        32397926,   # 1 year 9 days 23 hours 25 minutes 26 seconds
        38877512,   # 1 year 84 days 23 hours 18 minutes 32 seconds
        46653014,   # 1 year 174 days 23 hours 10 minutes 14 seconds
        55983617,   # 1 year 282 days 23 hours 17 seconds
        67180340    # 2 years 47 days 13 hours 12 minutes 20 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#cccccc"
),

"tokenmobiles-69": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-69",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        9936000,   # 115 days
        11923200,  # 138 days
        14307840   # 165 days 14 hours 24 minutes   
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=30000,
    rack_color="#ffffff"
),

"tokenmobiles-70": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-70",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        11145600,   # 129 days
        12260160,   # 141 days 21 hours 36 minutes
        13486176,   # 156 days 2 hours 9 minutes 36 seconds
        14834794,   # 171 days 16 hours 46 minutes 34 seconds
        16318273,   # 188 days 20 hours 51 minutes 13 seconds
        17950100,   # 207 days 18 hours 8 minutes 20 seconds
        19745110,   # 228 days 12 hours 45 minutes 10 seconds
        21719621,   # 251 days 9 hours 13 minutes 41 seconds
        23891583,   # 276 days 12 hours 33 minutes 3 seconds
        26280742,   # 304 days 4 hours 12 minutes 22 seconds
        28908816,   # 334 days 14 hours 13 minutes 36 seconds
        31799698,   # 1 year 3 days 1 hour 14 minutes 58 seconds
        34979667,   # 1 year 39 days 20 hours 34 minutes 27 seconds
        38477634,   # 1 year 80 days 8 hours 13 minutes 54 seconds
        42325397,   # 1 year 124 days 21 hours 3 minutes 17 seconds
        46557937    # 1 year 173 days 20 hours 45 minutes 37 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#5d8ae7"
),

"tokenmobiles-71": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-71",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        24624000,   # 285 days
        36936000,   # 1 year 62 days 12 hours
        55404000,   # 1 year 276 days 6 hours
        83106000    # 2 years 231 days 21 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#b39559"
),

"tokenmobiles-72": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-72",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        22982400,    # 266 days
        29877120,    # 345 days 19 hours 12 minutes
        38840256,    # 1 year 84 days 12 hours 57 minutes 36 seconds
        50492333,    # 1 year 219 days 9 hours 38 minutes 53 seconds
        65640033,    # 2 years 29 days 17 hours 20 minutes 33 seconds
        85332042,    # 2 years 257 days 15 hours 20 minutes 42 seconds
        110931655,   # 3 years 188 days 22 hours 20 minutes 55 seconds
        144211152,   # 4 years 209 days 2 hours 39 minutes 12 seconds
        187474497,   # 5 years 344 days 20 hours 14 minutes 57 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#f53041"
),

"tokenmobiles-73": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-73",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        6739200,   # 78 days
        7413120    # 85 days 19 hours 12 minutes
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffffff"
),

"tokenmobiles-74": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-74",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        21513600,    # 249 days
        30119040,    # 348 days 14 hours 24 minutes
        42166656,    # 1 year 123 days 57 minutes 36 seconds
        59033318,    # 1 year 318 days 6 hours 8 minutes 38 seconds
        82646646,    # 2 years 226 days 13 hours 24 minutes 6 seconds
        115705304,   # 3 years 244 days 4 hours 21 minutes 44 seconds
        161987426,   # 5 yaers 49 days 20 hours 30 minutes 26 seconds
        226782396,   # 7 years 69 days 19 hours 6 minutes 36 seconds
        317495354,   # 10 years 24 days 17 hours 9 minutes 14 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=20000,
    rack_color="#666666"
),

"tokenmobiles-75": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-75",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        11059200,   # 128 days
        13271040,   # 153 days 14 hours 24 minutes
        15925248,   # 184 days 7 hours 40 minutes 48 seconds
        19110298,   # 221 days 4 hours 24 minutes 58 seconds
        22932357,   # 265 days 10 hours 5 minutes 57 seconds
        27518829,   # 318 days 12 hours 7 minutes 9 seconds
        33022594,   # 1 year 17 days 4 hours 56 minutes 34 seconds
        39627113,   # 1 year 93 days 15 hours 31 minutes 53 seconds
        47552536,   # 1 year 185 days 9 hours 2 minutes 16 seconds
        57063043,   # 1 year 295 days 10 hours 50 minutes 43 seconds
        68475651    # 2 years 62 days 13 hours 51 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=1000,
    rack_color="#01a60c"
),

"tokenmobiles-76": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-76",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        21686400,    # 251 days
        32529600,    # 1 year 11 days 12 hours
        48794400,    # 1 year 199 days 18 hours
        73191600,    # 2 years 117 days 3 hours
        109787400,   # 3 years 175 days 16 hours 30 minutes
        164681100    # 5 years 81 days 45 minutes
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#ffd300"
),

"tokenmobiles-77": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-77",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16329600,    # 189 days
        21228480,    # 245 days 16 hours 48 minutes
        27597024,    # 319 days 9 hours 50 minutes 24 seconds
        35876131,    # 1 year 50 days 5 hours 35 minutes 31 seconds
        46638971,    # 1 year 174 days 19 hours 16 minutes 11 seconds
        60630662,    # 1 year 336 days 17 hours 51 minutes 2 seconds
        78819860,    # 2 years 182 days 6 hours 24 minutes 20 seconds
        102465818,   # 3 years 90 days 22 hours 43 minutes 38 seconds
        133205564,   # 4 years 81 days 17 hours 32 minutes 44 seconds
        173167233,   # 5 years 179 days 6 hours 33 seconds
        225117403,   # 7 years 50 days 12 hours 36 minutes 43 seconds
        292652624,   # 9 years 102 days 4 hours 23 minutes 44 seconds
        380448411    # 12 years 23 days 8 hours 6 minutes 51 seconds
    ],

    boost_percent=30,
    supply_current=1,
    supply_total=5000,
    rack_color="#73500c"
),

"tokenmobiles-78": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-78",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16502400,   # 191 days
        19802880,   # 229 days 4 hours 48 minutes
        23763456,   # 275 days 57 minutes 36 seconds
        28516147,   # 330 days 1 hour 9 minutes 7 seconds
        34219377,   # 1 year 31 days 1 hour 22 minutes 57 seconds
        41063252,   # 1 year 110 days 6 hours 27 minutes 32 seconds
        49275902,   # 1 year 205 days 7 hours 45 minutes 2 seconds
        59131083    # 1 yaer 319 days 9 hours 18 minutes 3 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#cccccc"
),

"tokenmobiles-79": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-79",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        14688000,   # 170 days
        17625600,   # 204 days
        21150720,   # 244 days 19 hours 12 minutes
        25380864,   # 293 days 18 hours 14 minutes 24 seconds
        30457037,   # 352 days 12 hours 17 minutes 17 seconds
        36548444,   # 1 year 58 days 20 minutes 44 seconds
        43858133,   # 1 year 142 days 14 hours 48 minutes 53 seconds
        52629760,   # 1 year 244 days 3 hours 22 minutes 40 seconds
        63155712    # 2 years 23 hours 15 minutes 12 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#ff7300"
),

"tokenmobiles-80": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-80",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        11404800,   # 132 days
        12545280,   # 145 days 4 hours 48 minutes
        13799808,   # 159 days 17 hours 16 minutes 48 seconds
        15179789,   # 175 days 16 hours 36 minutes 29 seconds
        16697768,   # 193 days 6 hours 16 minutes 8 minutes
        18367544,   # 212 days 14 hours 5 minutes 44 seconds
        20204299,   # 233 days 20 hours 18 minutes 19 seconds
        22224729,   # 257 days 5 hours 32 minutes 9 seconds
        24447202,   # 282 days 22 hours 53 minutes 22 seconds
        26891922,   # 311 days 5 hours 58 minutes 42 seconds
        29581114,   # 342 days 8 hours 58 minutes 34 seconds
        32539225,   # 1 year 11 days 14 hours 40 minutes 25 seconds
        35793148,   # 1 year 49 days 6 hours 32 minutes 28 seconds
        39372463,   # 1 year 90 days 16 hours 47 minutes 43 seconds
        43309709,   # 1 year 136 days 6 hours 28 minutes 29 seconds
        47640680    # 1 year 186 days 9 hours 31 minutes 20 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=20000,
    rack_color="#ffffff"
),

"tokenmobiles-81": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-81",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        8640000,   # 100 days
        9504000,   # 110 days
        10454400   # 121 days
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#d1076a"
),

"tokenmobiles-82": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-82",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        7344000,   # 85 days
        8078400,   # 93 days 12 hours
        8886240    # 102 days 20 hours 24 minutes
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#295fcc"
),

"tokenmobiles-83": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-83",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        10108800,   # 117 days
        11119680,   # 128 days 16 hours 48 minutes
        12231648,   # 141 days 13 hours 40 minutes 48 seconds
        13454813,   # 155 days 17 hours 26 minutes 53 seconds
        14800294,   # 171 days 7 hours 11 minutes 34 seconds
        16280323,   # 188 days 10 hours 18 minutes 43 seconds
        17908356    # 207 days 6 hours 32 minutes 36 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#009999"
),

"tokenmobiles-84": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-84",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        11059200,   # 128 days
        12165120,   # 140 days 19 hours 12 minutes
        13381632,   # 154 days 21 hours 7 minutes 12 seconds
        14719795,   # 170 days 8 hours 49 minutes 55 seconds
        16191775,   # 187 days 9 hours 42 minutes 55 seconds
        17810952,   # 206 days 3 hours 29 minutes 12 seconds
        19592047,   # 226 days 18 hours 14 minutes 7 seconds
        21551252,   # 249 days 10 hours 27 minutes 32 seconds
        23706377,   # 274 days 9 hours 6 minutes 17 seconds
        26077015,   # 301 days 19 hours 36 minutes 55 seconds
        28684717,   # 331 days 23 hours 58 minutes 37 seconds
        31553188,   # 1 year 4 hours 46 minutes 28 seconds
        34708507,   # 1 year 36 days 17 hours 15 minutes 7 seconds
        38179358,   # 1 year 76 days 21 hours 22 minutes 38 seconds
        41997294,   # 1 year 121 days 1 hour 54 minutes 54 seconds
        46197023,   # 1 year 169 days 16 hours 30 minutes 23 seconds
        50816725    # 1 year 223 days 3 hours 45 minutes 25 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffffff"
),

"tokenmobiles-85": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-85",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        18748800,   # 217 days
        22498560,   # 260 days 9 hours 36 minutes
        26998272,   # 312 days 11 hours 31 minutes 12 seconds
        32397926,   # 1 year 9 days 23 hours 25 minutes 26 seconds
        38877512,   # 1 year 84 days 23 hours 18 minutes 32 seconds
        46653014,   # 1 year 174 days 23 hours 10 minutes 14 seconds
        55983617,   # 1 year 282 days 23 hours 17 seconds
        67180340,   # 2 years 47 days 13 hours 12 minutes 20 seconds
        80616408    # 2 years 203 days 1 hour 26 minutes 48 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=5000,
    rack_color="#cccccc"
),

"tokenmobiles-86": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-86",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        18057600,   # 209 days
        21669120,   # 250 days 19 hours 12 minutes
        26002944,   # 300 days 23 hours 2 minutes 24 seconds
        31203533,   # 361 days 3 hours 38 minutes 53 seconds
        37444239,   # 1 year 68 days 9 hours 10 minutes 39 seconds
        44933087,   # 1 year 155 days 1 hour 24 minutes 47 seconds
        53919705,   # 1 year 259 days 1 hour 41 minutes 45 seconds
        64703646,   # 2 years 18 days 21 hours 14 minutes 6 seconds
        77644375,   # 2 years 168 days 15 hours 52 minutes 55 seconds
        93173250,   # 2 years 348 days 9 hours 27 minutes 30 seconds
        111807900   # 3 years 199 days 1 hour 44 minutes 60 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=5000,
    rack_color="#ffffff"
),

"tokenmobiles-87": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-87",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        19440000,    # 225 days
        27216000,    # 315 days
        38102400,    # 1 year 76 days
        53343360,    # 1 year 252 days 9 hours 36 minutes
        74680704,    # 2 years 134 days 8 hours 38 minutes 24 seconds
        104552986,   # 3 years 115 days 2 hours 29 minutes 46 seconds
        146374180,   # 4 years 234 days 3 hours 29 minutes 40 seconds
        204923852,   # 6 years 181 days 19 hours 17 minutes 32 seconds
        286893392,   # 9 years 35 days 12 hours 36 minutes 32 seconds
        401650749    # 12 years 268 days 17 hours 39 minutes 9 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=1000,
    rack_color="#f53041"
),

"tokenmobiles-88": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-88",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        25056000,   # 290 days
        37584000,   # 1 year 70 days
        56376000,   # 1 year 287 days 12 hours
        84564000,   # 2 years 248 days 18 hours
        126846000   # 4 years 8 days 3 hours
    ],

    boost_percent=50,
    supply_current=1,
    supply_total=1000,
    rack_color="#fe0000"
),

"tokenmobiles-89": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-89",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        9676800,    # 112 days
        10644480,   # 123 days 4 hours 48 seconds
        11708928,   # 135 days 12 hours 28 minutes 48 seconds
        12879821,   # 149 days 1 hour 43 minutes 1 seconds
        14167803,   # 163 days 23 hours 30 minutes 3 seconds
        15584583,   # 180 days 9 hours 3 minutes 3 seconds
        17143041,   # 198 days 9 hours 57 minutes 21 seconds
        18857346,   # 218 days 6 hours 9 minutes 6 seconds
        20743080,   # 240 days 1 hour 58 minutes
        22817388    # 264 days 2 hours 9 minutes 48 seconds 
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=20000,
    rack_color="#ffffff"
),

"tokenmobiles-90": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-90",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        16848000,    # 195 days
        23587200,    # 273 days
        33022080,    # 1 year 17 days 4 hours 48 minutes
        46230912,    # 1 year 170 days 1 hour 55 minutes 12 seconds
        64723277,    # 2 years 19 days 2 hours 41 minutes 17 seconds
        90612588,    # 2 years 318 days 18 hours 9 minutes 48 seconds
        126857623,   # 4 years 8 days 6 hours 13 minutes 43 seconds
        177600672    # 5 years 230 days 13 hours 31 minutes 12 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=30000,
    rack_color="#ffbcef"
),

"tokenmobiles-91": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-91",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        10800000,   # 125 days
        11880000,   # 137 days 12 hours
        13068000,   # 151 days 6 hours
        14374800,   # 166 days 9 hours
        15812280,   # 183 days 18 minutes
        17393508,   # 201 days 7 hours 31 minutes 48 seconds
        19132859,   # 221 days 10 hours 40 minutes 59 seconds
        21046145,   # 243 days 14 hours 9 minutes 5 seconds
        23150759,   # 267 days 22 hours 45 minutes 59 seconds
        25465835,   # 294 days 17 hours 50 minutes 35 seconds
        28012419,   # 324 days 5 hours 13 minutes 39 seconds
        30813660,   # 356 days 15 hours 21 minutes
        33895026,   # 1 year 27 days 7 hours 17 minutes 6 seconds
        37284529,   # 1 year 66 days 12 hours 48 minutes 49 seconds
        41012982    # 1 year 109 days 16 hours 29 minutes 42 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#feee99"
),

"tokenmobiles-92": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-92",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00003,
    cycle_durations_seconds=[
        14601600,    # 169 days
        17521920,    # 202 days 19 hours 12 minutes
        21026304,    # 243 days 8 hours 38 minutes 24 seconds
        25231565,    # 292 days 46 minutes 5 seconds
        30277878,    # 350 days 10 hours 31 minutes 18 seconds
        36333453,    # 1 year 55 days 12 hours 37 minutes 33 seconds
        43600144,    # 1 year 139 days 15 hours 9 minutes 4 seconds
        52320173,    # 1 year 240 days 13 hours 22 minutes 53 seconds
        62784207,    # 1 year 361 days 16 hours 3 minutes 27 seconds
        75341049,    # 2 years 142 days 4 minutes 9 seconds
        90409259,    # 2 years 316 days 9 hours 40 minutes 59 seconds
        108491110,   # 3 years 160 days 16 hours 25 minutes 10 seconds
        130189332,   # 4 hours 46 days 19 hours 42 minutes 12 seconds
        156227199,   # 4 hours 348 days 4 hours 26 minutes 39 seconds
        187472639,   # 5 years 344 days 19 hours 43 minutes 59 seconds
        224967166,   # 7 years 48 days 18 hours 52 minutes 46 seconds
        269960599,   # 8 years 204 days 13 hours 3 minutes 19 seconds
        323952719,   # 10 years 99 days 10 hours 51 minutes 59 seconds
        388743263,   # 12 years 119 days 8 hours 14 minutes 23 seconds
        466491916    # 14 years 289 days 5 hours 5 minutes 16 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=300,
    rack_color="#f53041"
),

"tokenmobiles-93": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-93",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        20131200,    # 233 days
        28183680,    # 326 days 4 hours 48 minutes
        39457152,    # 1 year 91 days 16 hours 19 minutes 12 seconds
        55240013,    # 1 year 274 days 8 hours 26 minutes 53 seconds
        77336018,    # 2 years 165 days 2 hours 13 minutes 38 seconds
        108270425,   # 3 years 158 days 3 hours 7 minutes 5 seconds
        151578595,   # 4 years 294 days 9 hours 9 minutes 55 seconds
        212210033    # 6 years 266 days 3 hours 13 minutes 53 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=10000,
    rack_color="#ffffff"
),

"tokenmobiles-94": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-94",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        14342400,   # 166 days
        17210880,   # 199 days 4 hours 48 minutes
        20653056,   # 239 days 57 minutes 36 seconds
        24783667,   # 286 days 20 hours 21 minutes 7 seconds
        29740401,   # 344 days 5 hours 13 minutes 21 seconds
        35688480,   # 1 year 48 days 1 hour 28 minutes
        42826177,   # 1 year 130 days 16 hours 9 minutes 37 seconds
        51391412,   # 1 year 229 days 19 hours 23 minutes 32 seconds
        61669695    # 1 year 348 days 18 hours 28 minutes 15 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=10000,
    rack_color="#99bcff"
),

"tokenmobiles-95": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-95",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        21600000,    # 250 days
        30240000,    # 350 days
        42336000,    # 1 year 125 days
        59270400,    # 1 year 321 days
        82978560,    # 2 years 230 days 9 hours 36 minutes
        116169984,   # 3 years 249 days 13 hours 26 minutes 24 seconds
        162637978,   # 5 years 57 days 9 hours 12 minutes 58 seconds
        227693169,   # 7 years 80 days 8 hours 6 minutes 9 seconds
        318770436    # 10 years 39 days 11 hours 20 minutes 36 seconds
    ],

    boost_percent=40,
    supply_current=1,
    supply_total=20000,
    rack_color="#ffe459"
),

"tokenmobiles-96": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-96",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        11664000,   # 135 days
        12830400,   # 148 days 12 hours
        14113440,   # 163 days 8 hours 24 minutes
        15524784,   # 179 days 16 hours 26 minutes 24 seconds
        17077262,   # 197 days 15 hours 41 minutes 2 seconds
        18784989,   # 217 days 10 hours 3 minutes 9 seconds
        20663488,   # 239 days 3 hours 51 minutes 28 seconds
        22729836    # 263 days 1 hour 50 minutes 36 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=10000,
    rack_color="#ff7300"
),

"tokenmobiles-97": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-97",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        6220800,   # 72 days
        6842880,   # 79 days 4 hours 48 minutes
        7527168    # 87 days 2 hours 52 minutes 48 seconds
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=1000,
    rack_color="#68cd3f"
),

"tokenmobiles-98": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-98",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        13132800,   # 152 days
        15759360,   # 182 days 9 hours 36 minutes
        18911232,   # 218 days 21 hours 7 minutes 12 seconds
        22693478,   # 262 days 15 hours 44 minutes 38 seconds
        27232174,   # 315 days 4 hours 29 minutes 34 seconds
        32678609,   # 1 year 13 days 5 hours 23 minutes 29 seconds
        39214331,   # 1 year 88 days 20 hours 52 minutes 11 seconds
        47057197    # 1 year 179 days 15 hours 26 minutes 37 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=20000,
    rack_color="#ffffff"
),

"tokenmobiles-99": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-99",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        15292800,     # 177 days
        18351360,     # 212 days 9 hours 36 minutes
        22021632,     # 254 days 21 hours 7 minutes 12 seconds
        26425958,     # 305 days 20 hours 32 minutes 38 seconds
        31711150,     # 1 year 2 days 39 minutes 10 seconds
        38053380,     # 1 year 75 days 10 hours 23 minutes
        45664056,     # 1 year 163 days 12 hours 27 minutes 36 seconds
        54796867,     # 1 year 269 days 5 hours 21 minutes 7 seconds
        65756241,     # 2 years 31 days 1 hour 37 minutes 21 seconds
        78907489,     # 2 years 183 days 6 hours 44 minutes 49 seconds
        94688987,     # 3 years 22 hours 29 minutes 47 seconds
        113626784,    # 3 years 220 days 2 hours 59 minutes 44 seconds
        136352141,    # 4 years 118 days 3 hours 35 minutes 41 seconds
        163622569,    # 5 years 68 days 18 hours 42 minutes 49 seconds
        196347083,    # 6 years 82 days 12 hours 51 minutes 23 seconds
        235616500     # 7 years 172 days 1 hour 1 minute 40 seconds
    ],

    boost_percent=20,
    supply_current=1,
    supply_total=5000,
    rack_color="#b39559"
),

"tokenmobiles-100": TokenmobileConfig(
    rack_id="SP3X384EHYMSQPRKZE2R61J81V0G11KTMKDZTS8NK.tokenmobiles-100",
    start_timestamp=datetime.now(tz=timezone.utc).timestamp(),
    value_increment_per_minute=0.00001,
    cycle_durations_seconds=[
        5184000   # 60 days
    ],

    boost_percent=10,
    supply_current=1,
    supply_total=50000,
    rack_color="#2020fe"
),











}
# ========================
# ENGINE
# ========================

def format_timer(seconds: int) -> str:
    seconds = max(0, seconds)

    years = seconds // (365 * 24 * 3600)
    seconds %= (365 * 24 * 3600)

    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    return f"{years:02}:{days:03}:{hours:02}:{minutes:02}:{seconds:02}"


def resolve_rack_state(config: TokenmobileConfig, now_ts=None) -> dict:
    if now_ts is None:
        now_ts = datetime.now(tz=timezone.utc).timestamp()

    elapsed = int(now_ts - config.start_timestamp)
    if elapsed < 0:
        elapsed = 0

    total_cycles = len(config.cycle_durations_seconds)
    cycle_start = 0

    for idx, duration in enumerate(config.cycle_durations_seconds):
        if elapsed < cycle_start + duration:
            cycle_elapsed = elapsed - cycle_start
            minutes = cycle_elapsed // 60
            value = minutes * config.value_increment_per_minute

            cycle_end_display = format_timer(duration)

            return {
                "rack_id": config.rack_id,
                "rack_color": config.rack_color,
                "cycle_index": idx + 1,
                "cycles_total": total_cycles,
                "remaining_cycles": total_cycles - (idx + 1),
                "timer": format_timer(cycle_elapsed),
                "value": f"₿{value:.5f}",
                "cycle_end_display": cycle_end_display,
                "boost_percent": config.boost_percent,
                "supply_current": config.supply_current,
                "supply_total": config.supply_total,
                "frozen": False
            }

        cycle_start += duration

    final_duration = config.cycle_durations_seconds[-1]
    final_minutes = final_duration // 60
    final_value = final_minutes * config.value_increment_per_minute

    return {
        "rack_id": config.rack_id,
        "rack_color": config.rack_color,
        "cycle_index": total_cycles,
        "cycles_total": total_cycles,
        "remaining_cycles": 0,
        "timer": format_timer(final_duration),
        "value": f"₿{final_value:.5f}",
        "boost_percent": config.boost_percent,
        "supply_current": config.supply_current,
        "supply_total": config.supply_total,
        "cycle_end_display": "",
        "frozen": True
    }

# ========================
# WEB SERVER
# ========================

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/rack/<rack_name>")
def rack_data(rack_name):

    config = RACKS.get(rack_name)

    if not config:
        return jsonify({
            "error": "Rack not found"
        }), 404

    return jsonify(resolve_rack_state(config))


@app.route("/racks")
def all_racks():

    return jsonify([
        resolve_rack_state(config)
        for config in RACKS.values()
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
