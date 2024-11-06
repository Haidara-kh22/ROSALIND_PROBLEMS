def probability_of_dominant(k, m, n):
    total = k + m + n

    # Probability of each mating combination producing dominant offspring
    prob_dominant = 0

    # AA and AA
    prob_dominant += (k / total) * ((k - 1) / (total - 1))

    # AA and Aa
    prob_dominant += (k / total) * (m / (total - 1)) * 1  # Produces dominant
    prob_dominant += (m / total) * (k / (total - 1)) * 1  # Produces dominant

    # AA and aa
    prob_dominant += (k / total) * (n / (total - 1)) * 1  # Produces dominant
    prob_dominant += (n / total) * (k / (total - 1)) * 1  # Produces dominant

    # Aa and Aa
    prob_dominant += (m / total) * ((m - 1) / (total - 1)) * 0.75

    # Aa and aa
    prob_dominant += (m / total) * (n / (total - 1)) * 0.5
    prob_dominant += (n / total) * (m / (total - 1)) * 0.5

    # aa and aa (no dominant offspring)
    
    return prob_dominant

# Example usage:
k = 19  # homozygous dominant
m = 29  # heterozygous
n = 24  # homozygous recessive
print(probability_of_dominant(k, m, n))
