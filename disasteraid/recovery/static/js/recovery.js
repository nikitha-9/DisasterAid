document.addEventListener('DOMContentLoaded', () => {
    const newsFeed = document.getElementById('news-feed');

    // Sample news data (in a real app, this would come from a server)
    const news = [
        {
            title: 'Federal Aid Approved for пострадавшие Counties',
            description: 'FEMA has approved individual assistance for residents of several counties affected by the recent floods.',
            date: '2025-05-28',
            link: '#'
        },
        {
            title: 'Volunteer Cleanup Efforts Underway',
            description: 'Volunteers are needed to help with debris removal and cleanup in affected areas.  Sign up today!',
            date: '2025-05-27',
            link: '#'
        },
        {
            title: 'Disaster Recovery Centers Open',
            description: 'Disaster Recovery Centers are now open in пострадавшие areas to provide information and assistance.',
            date: '2025-05-26',
            link: '#'
        },
         {
            title: 'State Announces New Housing Assistance Program',
            description: 'The state government has announced a new program to provide temporary housing assistance to displaced residents.',
            date: '2025-05-29',
            link: '#'
        }
    ];

    // Function to create a news item
    function createNewsItem(item) {
        const newsItem = document.createElement('div');
        newsItem.className = 'news-item';

        const title = document.createElement('h3');
        const titleLink = document.createElement('a');
        titleLink.textContent = item.title;
        titleLink.href = item.link;  // Add the link here
        title.appendChild(titleLink);

        const description = document.createElement('p');
        description.textContent = item.description;

        const date = document.createElement('span');
        date.textContent = item.date;

        newsItem.appendChild(title);
        newsItem.appendChild(description);
        newsItem.appendChild(date);

        return newsItem;
    }

    // Add news items to the feed
    news.forEach(item => {
        newsFeed.appendChild(createNewsItem(item));
    });
});