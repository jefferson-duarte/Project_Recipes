function my_scorpe() {
    const forms = document.querySelectorAll('.form-delete');

    for (const form of forms) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            const confirmed = confirm('Are you sire?');

            if (confirmed) {
                form.submit();
            }
        });
    }
}

my_scorpe();