def top_servers(logs, k):
    servers_frequency = {}
    for log in logs:
        server_name = log.split('-')[0]
        if server_name in servers_frequency:
            servers_frequency[server_name] += 1
        else:
            servers_frequency[server_name] = 1

    servers = sorted(servers_frequency.items(), key=lambda item: item[0])
    servers = sorted(servers, key=lambda item: item[1], reverse=True)

    return [ server[0] for server in servers ][:k]

def test_top_servers():
    arr = [ "a-23", "c-45", "c-56", "b-24", "a-ert", "b-er", "c-car",]
    servers = top_servers(arr, 2)
    assert servers == ["c", "a"]