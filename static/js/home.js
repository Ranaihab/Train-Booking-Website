function loadData() {
    return eval(JSON.parse(document.getElementById('trips-data').textContent));
}

function reset() {
    var trips = loadData();
    for (var trip in trips) {
        var idExists = !!document.getElementById(trips[trip]['pk']);
        if (idExists) {
            document.getElementById(trips[trip]['pk']).style.display = '';
        }
    }
    document.getElementById("dateOption").value = '';
    document.getElementById("sourceOption").value = 'stations';
    document.getElementById("destOption").value = 'stations';
    document.getElementById("timeOption").value = '';
    document.getElementById("seatNbOption").value = '';
}

function filter() {
    var trips = loadData();
    console.log(trips);
    var date = document.getElementById("dateOption").value;
    var source = document.getElementById("sourceOption").value;
    var dest = document.getElementById("destOption").value;
    var time = document.getElementById("timeOption").value;
    var seatNb = document.getElementById("seatNbOption").value;
    var idExists;
    if(source == dest && source != 'stations'){
        alert("Source and Destination can't be the same.");
        return;
    }
    for (var trip in trips) {
        idExists = !!document.getElementById(trips[trip]['pk']);
        if (date != '' && trips[trip]['fields']['source'] != date) {
            if (idExists) {
                document.getElementById(trips[trip]['pk']).style.display = 'none';
            }
        }
        if (source != 'stations' && trips[trip]['fields']['source'] != source) {
            if (idExists) {
                document.getElementById(trips[trip]['pk']).style.display = 'none';
            }
        }
        if (dest != 'stations' && trips[trip]['fields']['destination'] != dest) {
            if (idExists) {
                document.getElementById(trips[trip]['pk']).style.display = 'none';
            }
        }
        if (time != '' && trips[trip]['fields']['start_Time'].slice(0,2) != time.slice(0,2)) {
            if (idExists) {
                document.getElementById(trips[trip]['pk']).style.display = 'none';
            }
        }
        if (seatNb != '' && trips[trip]['fields']['Remaining_seats'] < seatNb) {
            if (idExists) {
                document.getElementById(trips[trip]['pk']).style.display = 'none';
            }
        }
    }
}