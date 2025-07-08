import scratchattach as sa
server = sa.init_cloud_server(
    '127.0.0.1', 8080, 
    thread=True, 
    length_limit=None, allow_non_numeric=False,
    whitelisted_projects=None, allow_nonscratch_names=False, blocked_ips=[],
    sync_players=True, # when set to False, other players will no longer be notified about cloud updates (only the server will see and parse them)
    log_var_sets=True # when set to True, all var sets will be printed to the console (can be spammy)
)
server.start()
