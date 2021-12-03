
def sort_carries(carries):
    sorted_results = {"loss": [], "no_gain": [], "short_gain": [], "med_gain": [], "big_gain": []}

    for carry in carries:
        if carry < 0:
            sorted_results["loss"].append(carry)
        elif carry == 0:
            sorted_results["no_gain"].append(carry)
        elif 0 < carry < 5:
            sorted_results["short_gain"].append(carry)
        elif 5 <= carry < 10:
            sorted_results["med_gain"].append(carry)
        elif carry >= 10:
            sorted_results["big_gain"].append(carry)

    return sorted_results


def bucket_carry_counts(raw_carries):
    sorted_carries = sort_carries(raw_carries)
    bucketed_carries = {'loss': len(sorted_carries['loss']),
                        'no_gain': len(sorted_carries['no_gain']),
                        'short_gain': len(sorted_carries['short_gain']),
                        'med_gain': len(sorted_carries['med_gain']),
                        'big_gain': len(sorted_carries['big_gain'])}
    return bucketed_carries
