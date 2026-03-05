from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("receiver", "0001_initial"),
    ]

    operations = [
        # 3 days chunk interval
        migrations.RunSQL(
            "SELECT create_hypertable('\"receiver_data\"', 'time', chunk_time_interval => INTERVAL '3 days');"
        ),
        migrations.RunSQL(
            "ALTER TABLE \"receiver_data\" \
                SET (timescaledb.compress, \
                timescaledb.compress_segmentby = 'station_id, measurement_id, base_time');"
        ),
        # Compress after 7 days
        migrations.RunSQL(
            "SELECT add_compression_policy('\"receiver_data\"', INTERVAL '7 days');"
        ),
    ]
