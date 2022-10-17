# MODULES ===========================================================
import toml
# FUNCTIONS =========================================================
def get_key(header, key) -> str:
    with open('./properties.toml', 'r') as f:
        data = toml.loads(f.read())
        data = data[header][key]
    return data
