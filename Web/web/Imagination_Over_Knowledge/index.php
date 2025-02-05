<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini CTF Challenge</title>
    <link rel="stylesheet" href="style.css">
    <style>
        .hint {
            margin-top: 10px;
            display: none;
            color: yellow;
        }
        .btn {
            padding: 10px 20px;
            background-color: #61dafb;
            color: #000;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover {
            background-color: #21a1f1;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Mini CTF Challenge</h1>
        <p>Can you find the flag?</p>
        <p id="message">
            <?php
                if (isset($_GET['flag'])) {
                    $flag = $_GET['flag'];
                    if ($flag === 'shellmates' || $flag === 'shellmates.txt') {
                        echo "Flag: SHELLMATES{E3MC2_1MAG1NAT10N_1S_P0W3RFUL_42}";
                    } else {
                        echo "Invalid file. Try again!";
                    }
                } else {
                    echo "Find me haha.";
                }
            ?>
        </p>
        <button class="btn" onclick="showHint()">Show Hint</button>
        <p class="hint" id="hint">Hint: Which club learn with him cyber security in algeria? </p>
    </div>
    <script>
        function showHint() {
            document.getElementById('hint').style.display = 'block';
        }
    </script>
</body>
</html>

