document.addEventListener('DOMContentLoaded', () => {
    const alertFeed = document.getElementById('alert-feed');

    // Sample alert data (in a real app, this would come from a server)
    const alerts = [
        {
            type: 'warning',
            title: 'Severe Thunderstorm Warning',
            message: 'Issued for your county. Seek shelter immediately.',
            date: '2025-05-20',
        },
        {
            type: 'info',
            title: 'Earthquake Preparedness Drill',
            message: 'Remember to Drop, Cover, and Hold On!',
            date: '2025-05-22',
        },
        {
            type: 'danger',
            title: 'Flash Flood Emergency',
            message: 'Evacuate to higher ground immediately!',
            date: '2025-05-21',
        },
        {
            type: 'info',
            title: 'Hurricane Season Begins June 1st',
            message: 'Prepare your hurricane preparedness kit and review your family plan.',
            date: '2025-05-25'
        }
    ];

    // Function to create an alert item
    function createAlertItem(alert) {
        const alertItem = document.createElement('div');
        alertItem.className = 'alert-item';

        if (alert.type === 'info') {
            alertItem.classList.add('info');
        } else if (alert.type === 'warning') {
            alertItem.classList.add('warning');
        } else if (alert.type === 'danger') {
            alertItem.classList.add('danger');
        }

        const title = document.createElement('h3');
        title.innerHTML = `<i class="fas fa-exclamation-triangle"></i> ${alert.title}`;

        if (alert.type === 'info') {
            title.innerHTML = `<i class="fas fa-info-circle"></i> ${alert.title}`;
        }
        if (alert.type === 'danger'){
            title.innerHTML = `<i class="fas fa-ban"></i> ${alert.title}`;
        }

        const message = document.createElement('p');
        message.textContent = alert.message;

        const date = document.createElement('span');
        date.textContent = alert.date;

        alertItem.appendChild(title);
        alertItem.appendChild(message);
        alertItem.appendChild(date);

        return alertItem;
    }

    // Add alerts to the feed
    alerts.forEach(alert => {
        alertFeed.appendChild(createAlertItem(alert));
    });
});