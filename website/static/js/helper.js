$(document).ready(function () {

    // Format Rupiah
    $('.price-formatted').each(function() {
        var formattedPrice = formatRupiah($(this).text(), 'Rp. ');
        $(this).text(formattedPrice);
    });

    $('.price-formatted-kg').each(function() {
        var formattedPrice = formatRupiah($(this).text(), 'Rp. ');
        $(this).text(formattedPrice + '/kg');
    });
})

formatRupiah = (angka, prefix, suffix) => {

    if (suffix == undefined) {
        suffix = '';
    }

    if (typeof angka === 'number') {
        angka = angka.toString();
    }

    var number_string = angka.replace(/[^,\d]/g, '').toString(),
        split = number_string.split(','),
        sisa = split[0].length % 3,
        rupiah = split[0].substr(0, sisa),
        ribuan = split[0].substr(sisa).match(/\d{3}/gi);

    if (ribuan) {
        separator = sisa ? '.' : '';
        rupiah += separator + ribuan.join('.');
    }

    rupiah = split[1] != undefined ? rupiah + ',' + split[1] : rupiah;
    return prefix == undefined 
        ? rupiah + suffix 
        : (rupiah ? 'Rp. ' + rupiah + suffix : '');
}


