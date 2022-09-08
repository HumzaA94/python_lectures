if __name__ == "__main__":
    list_ = [
        "Crosby shot the puck twice.",
        "random weather today",
        "2 shots nothing to show.",
        "SHOTS! GOAL!",
        "shots",
        "goal",
        "goals",
        "Shots",
        "assists",
        "assist",
    ]

    TARGET_LIST = ["shot", "goal", "assist"]
    count_dict = {"shot": 0, "goal": 0, "assist": 0}
    for value in list_:
        value = value.lower().strip()
        print(value)
        for target_value in TARGET_LIST:
            if target_value in value:
                count_dict[target_value] += 1
print("a")
