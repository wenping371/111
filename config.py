# Configuration file for target websites, filter rules, and storage settings

# Target websites configuration
TARGET_WEBSITES = {
    "website1": {
        "url": "https://www.example1.com",
        "check_frequency": "daily"
    },
    "website2": {
        "url": "https://www.example2.com",
        "check_frequency": "weekly"
    }
}

# Filter rules
FILTER_RULES = [
    {
        "type": "keyword",
        "pattern": "example"
    },
    {
        "type": "exclude",
        "pattern": "unwanted"
    }
]

# Storage settings
STORAGE_SETTINGS = {
    "type": "local",
    "path": "./storage/data.json"
}