file_path = "data/server_usage.txt"

print("SERVER DISK USAGE REPORT")
print("========================")

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()

        server_name, usage = line.split(",")

        usage = int(usage)

        if usage >= 80:
            print(f"WARNING: {server_name} is at {usage}% disk usage")
        else:
            print(f"OK: {server_name} is at {usage}% disk usage")
