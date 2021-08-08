# Module: main
# Author:
# Version: 0.1
# Created on: 08.08.2021
# License: The Unlicense
# 

"""

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

"""



"""
Example video plugin that is compatible with Kodi 19.x "Matrix" and above
"""
import sys
from urllib.parse import urlencode, parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_URL = sys.argv[0]
# Get the plugin handle as an integer number.
_HANDLE = int(sys.argv[1])

# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.

VIDEOS = {'The Alex Jones Show': [{'name': 'Aug 7, 2021 - Emergency Broadcast: Infrastructure Bill Containing Martial Law Provisions Set To Pass',
                       'thumb': 'https://assets.infowarsmedia.com/images/bb7b6057-60cd-4d65-b226-38a93b17c42e-large.jpg',
                       'video': 'https://downloads.banned.video/videos/2f8f2201-1995-4dd5-8afb-7b62f6349684.mp4',
                       'genre': 'News'},
                      {'name': 'Aug 6, 2021 - Global Bombshell! Israel & Australia Report All Covid Hospitalizations Are Vaccinated – FULL SHOW 8/6/21',
                       'thumb': 'https://assets.infowarsmedia.com/images/bb7b6057-60cd-4d65-b226-38a93b17c42e-large.jpg',
                       'video': 'https://downloads.banned.video/videos/d33657c3-ebb9-4b33-aa21-9e01cc0feedf.mp4',
                       'genre': 'News'},
                      {'name': 'Aug 6, 2021 - EXCLUSIVE: Mike Lindell Release New Information He Says will Overturn 2020 Election',
                       'thumb': 'https://assets.infowarsmedia.com/images/bb7b6057-60cd-4d65-b226-38a93b17c42e-large.jpg',
                       'video': 'https://downloads.banned.video/videos/9e86da25-bb04-4eb7-969f-f4b22eb2045d.mp4',
                       'genre': 'News'}
                      ],
          'War Room With Owen Shroyer': [{'name': 'HIGHLIGHTS - What On Earth Is Luciferase?!',
                      'thumb': 'https://assets.infowarsmedia.com/images/91a07c57-4dd3-4fc5-8022-cb866164b140-large.jpg',
                      'video': 'https://downloads.banned.video/videos/4cab556b-6210-45a0-95ae-2b09168ebb23.mp4',
                      'genre': 'News'},
                     {'name': 'Are We Living In Matthew Chapter 24?',
                      'thumb': 'https://assets.infowarsmedia.com/images/91a07c57-4dd3-4fc5-8022-cb866164b140-large.jpg',
                      'video': 'https://downloads.banned.video/videos/099e5c46-7b30-4a66-befd-2eaa2a046db9.mp4',
                      'genre': 'News'},
                     {'name': 'Satanic Church Sues For the Right To Ritual Abortion',
                      'thumb': 'https://assets.infowarsmedia.com/images/91a07c57-4dd3-4fc5-8022-cb866164b140-large.jpg',
                      'video': 'https://downloads.banned.video/videos/acff4b84-0433-4027-af64-87ba79864f78.mp4',
                      'genre': 'News'}
                     ],
          'InfoWarsFilms': [{'name': 'Endgame: Blueprint for Global Enslavement',
                      'thumb': 'https://assets.infowarsmedia.com/images/ac917c98-5469-40bf-8bf6-6d7c52ce8d92-large.jpg',
                      'video': 'https://downloads.banned.video/videos/908d8bab-24ad-409f-91bd-11ff9f152fd0.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'The Obama Deception',
                      'thumb': 'https://assets.infowarsmedia.com/images/6e60cbaa-2e1c-47ff-b338-ed20ea9b96b9-large.jpg',
                      'video': 'https://downloads.banned.video/videos/1d5801cc-95cc-42df-bcab-9be6100ff35f.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'America Destroyed by Design',
                      'thumb': 'https://assets.infowarsmedia.com/images/8b82bf09-0b0c-4191-8165-5ffa3a5e3f74-large.jpg',
                      'video': 'https://downloads.banned.video/videos/16a1a0c5-bf2c-4ad1-aacd-414277b224a6.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'Dark Secrets Inside Bohemian Grove',
                      'thumb': 'https://assets.infowarsmedia.com/images/26706292-bf02-4942-bd96-26464527ae84-large.jpg',
                      'video': 'https://downloads.banned.video/videos/13be9470-3386-4edf-a434-491c08d9dba9.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'LOOSE CHANGE 2',
                      'thumb': 'https://assets.infowarsmedia.com/images/35892cd6-7278-44d3-8493-47481d6f3ea6-large.jpg',
                      'video': 'https://downloads.banned.video/videos/dac9f0b2-306e-4c60-adf3-a651cf55d42f.mp4',
                      'genre': 'Documentaries'},
                     {'name': '9/11 The Road To Tyranny',
                      'thumb': 'https://assets.infowarsmedia.com/images/b695f9f8-3fba-4789-8f59-d75c8e3175e7-large.jpg',
                      'video': 'https://downloads.banned.video/videos/365f7df9-18b3-4e97-a49a-890cae46443e.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'Martial Law 911 Rise of The Police State',
                      'thumb': 'https://assets.infowarsmedia.com/images/d07a3877-7f94-426d-8858-d88255bfdace-large.jpg',
                      'video': 'https://downloads.banned.video/videos/a1975e94-711a-4212-abf4-1402b5980fa2.mp4',
                      'genre': 'Documentaries'},
                     {'name': '9/11 CHRONICLES: Truth Rising',
                      'thumb': 'https://assets.infowarsmedia.com/images/ca4aac4b-b082-489b-8dce-0fd2593e2f46-large.jpg',
                      'video': 'https://downloads.banned.video/videos/283bdb4d-f7b9-48e7-80e5-ff30c047261c.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'Ben Livingston: The Father Of Weaponized Weather',
                      'thumb': 'https://assets.infowarsmedia.com/images/a78f503a-b2df-424a-94f1-ababe433161d-large.png',
                      'video': 'https://downloads.banned.video/videos/283d53a4-1b21-491d-92eb-fcd3a3293704.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'The Order of Death',
                      'thumb': 'https://assets.infowarsmedia.com/images/fcd5f100-26bc-4a2a-84ff-4af922a38e51-large.jpg',
                      'video': 'https://downloads.banned.video/videos/20e3f6c6-12c9-4392-b466-c5fb0611b105.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'TERRORSTORM - A History Of Government Sponsored Terror',
                      'thumb': 'https://assets.infowarsmedia.com/images/5021a81b-7161-4dae-9f15-c6658fb51c61-large.jpg',
                      'video': 'https://downloads.banned.video/videos/ad180cf9-9e14-42a9-9d31-4d026058e5a2.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'Charlotte Iserbyt - The Deliberate Dumbing Down of America',
                      'thumb': 'https://assets.infowarsmedia.com/images/3b25eac6-d485-436e-8366-626f46d8bf5f-large.jpg',
                      'video': 'https://downloads.banned.video/videos/35d267bf-6362-4f62-a59a-51cb35ff8927.mp4',
                      'genre': 'Documentaries'},
                     {'name': 'The Cosmic Hoax: An Exposé',
                      'thumb': 'https://assets.infowarsmedia.com/images/99542494-07a6-4151-946d-27b7ad161d70-large.png',
                      'video': 'https://downloads.banned.video/videos/d728bd8d-366e-435b-a165-aad71b2a9d9e.mp4',
                      'genre': 'Documentaries'}
                     ],
         'The David Knight Show': [{'name': 'VIRAL LOAD? IT’S A LOAD OF BS',
                      'thumb': 'https://static-3.bitchute.com/live/channel_images/9c7qJvwx7YQ2/9rxJX8TPnIP9uv7Pn9eIVQiq_small.jpg',
                      'video': 'https://seed163.bitchute.com/9c7qJvwx7YQ2/xRVYfsaJzr9F.mp4',
                      'genre': 'News'},
                      {'name': 'SAFETY CULT: BREATHALYZER FOR EVERY NEW CAR',
                      'thumb': 'https://static-3.bitchute.com/live/channel_images/9c7qJvwx7YQ2/9rxJX8TPnIP9uv7Pn9eIVQiq_small.jpg',
                      'video': 'https://seed122.bitchute.com/9c7qJvwx7YQ2/BsnJ6JubSfUr.mp4',
                      'genre': 'News'}
                     ]}
                     
def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :return: plugin call URL
    :rtype: str
    """
    return '{}?{}'.format(_URL, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or API.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or API.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_HANDLE, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_HANDLE, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_HANDLE)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_HANDLE, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_HANDLE, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_HANDLE)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_HANDLE, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
