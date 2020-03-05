def merge_ranges(meetings):

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    print('Sorted Meetings [1:]: ', sorted_meetings[1:])
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        print('Merged Meeting: ', merged_meetings[-1])
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        print('Current Meeting Start: ', current_meeting_start)
        print('Current Meeting End: ', current_meeting_end)
        print('Last Merged Meeting Start: ', last_merged_meeting_start)
        print('Last Merged Meeting End: ', last_merged_meeting_end)
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
            print('Overlap Merged Meeting: ', merged_meetings[-1])
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))
    print('Return Merged Meeting: ', merged_meetings[-1])
    return merged_meetings

merge_ranges([(1, 5), (2, 3)])