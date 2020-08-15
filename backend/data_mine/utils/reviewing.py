"""Functions related to reviewing memes for removal or the manual changing of weighting."""

# TODO: Low priority. Start later.


def staleness_routine() -> None:
    """
    Cyclically increase the staleness of all of the memes depending on their age and a voting heuristic.

    The staleness index depends on (in order of importance):

    - How liked the meme template is.
    - How many times the meme template has been seen.
    - How old the meme template is (up to a certain number of days). It is counter-balanced by "classics" code that
      re-surges old content occasionally, but even these classics are never as fresh as when they were just uploaded.

    Notes
    -----
    This is not run frequently so it can be a bit slow.
    """

    raise NotImplementedError("staleness_routine is unimplemented.")
