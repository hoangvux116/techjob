def tag(job_title):
    title = job_title.lower()
    result = set()
    if "- hn" in title or "- hanoi" in title or "/hn" in title or "/hanoi" in title:
        result.add("Hanoi".lower())
    if "- hcmc" in title or "hcm" in title or "/hcmc" in title or "/hcm" in title:
        result.add("HoChiMinhCity".lower())
    if "- saigon" in title or "/saigon" in title:
        result.add("HoChiMinhCity".lower())
    if "remote" in title:
        result.add("Remote".lower())
    if "- ft" in title or "- full time" in title or "- fulltime" in title:
        result.add("FullTime".lower())
    if "- pt" in title or "/pt" in title or "- part time" in title or "- parttime" in title:
        result.add("PartTime".lower())
    if "- c -" in title:
        result.add("Contact".lower())
    list_tag = list(result)
    return list_tag