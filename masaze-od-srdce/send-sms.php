<?php
/**
 * Rezervační formulář — Masáže od srdce
 *
 * Posílá rezervaci jako e-mail na mmoravek00@volny.cz (krátká, čitelná)
 * + jako SMS přes SMSbrana.cz (pokud je nakonfigurováno SMSBRANA_LOGIN a SMSBRANA_PASSWORD)
 *
 * Konfigurace SMS brány: vyplňte konstanty SMSBRANA_LOGIN a SMSBRANA_PASSWORD níže.
 * Bez konfigurace formulář chodí jen e-mailem (mobil notifikace přes volny.cz e-mail).
 */
header('Content-Type: application/json; charset=utf-8');

// ===== KONFIGURACE =====
const TO_EMAIL       = 'mmoravek00@volny.cz';
const TO_PHONE       = '+420731827169';   // Milanův mobil
const FROM_EMAIL     = 'noreply@strankyprovas.cz';
const SMSBRANA_LOGIN = '';                 // doplnit, např. 'milan123'
const SMSBRANA_PASSWORD = '';              // doplnit (heslo na sms.sms-operator.cz nebo smsbrana.cz)
// ========================

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
  http_response_code(405);
  echo json_encode(['ok' => false, 'error' => 'Only POST allowed']);
  exit;
}

// Honeypot
$honeypot = trim($_POST['website'] ?? '');
if ($honeypot !== '') { echo json_encode(['ok' => true]); exit; }

$jmeno    = trim($_POST['jmeno']    ?? '');
$prijmeni = trim($_POST['prijmeni'] ?? '');
$telefon  = trim($_POST['telefon']  ?? '');
$delka    = trim($_POST['delka']    ?? '');
$cast_dne = trim($_POST['cast_dne'] ?? '');
$poznamka = trim($_POST['poznamka'] ?? '');

if ($jmeno === '' || $prijmeni === '' || $telefon === '' || $delka === '' || $cast_dne === '') {
  http_response_code(400);
  echo json_encode(['ok' => false, 'error' => 'Vyplňte prosím všechna povinná pole.']);
  exit;
}

$fullName = $jmeno . ' ' . $prijmeni;
$shortSms = "Rezervace: {$fullName}, {$delka}, {$cast_dne}. Tel: {$telefon}";
if ($poznamka !== '') { $shortSms .= ". Pozn: " . mb_substr($poznamka, 0, 60); }

$emailSubject = "Nová rezervace: {$fullName} — {$delka} ({$cast_dne})";
$emailBody = "NOVÁ REZERVACE z webu\n"
           . "============================\n\n"
           . "Jméno a příjmení: {$fullName}\n"
           . "Telefon:          {$telefon}\n"
           . "Délka masáže:     {$delka}\n"
           . "Část dne:         {$cast_dne}\n";
if ($poznamka !== '') { $emailBody .= "Poznámka:         {$poznamka}\n"; }
$emailBody .= "\nOdesláno: " . date('Y-m-d H:i:s') . "\n\n"
            . "— Automatická zpráva z webu masazeodsrdce.cz —";

$headers = [
  'From: Masáže od srdce <' . FROM_EMAIL . '>',
  'Reply-To: ' . $telefon . ' <' . FROM_EMAIL . '>',
  'Content-Type: text/plain; charset=utf-8',
  'MIME-Version: 1.0',
];

$emailOk = @mail(
  TO_EMAIL,
  '=?UTF-8?B?' . base64_encode($emailSubject) . '?=',
  $emailBody,
  implode("\r\n", $headers)
);

// SMS přes SMSbrana.cz (pokud nakonfigurováno)
$smsOk = null;
if (SMSBRANA_LOGIN !== '' && SMSBRANA_PASSWORD !== '') {
  $smsUrl = 'https://api.smsbrana.cz/smsconnect/http.php?'
          . 'login=' . urlencode(SMSBRANA_LOGIN)
          . '&password=' . urlencode(SMSBRANA_PASSWORD)
          . '&action=send_sms'
          . '&number=' . urlencode(TO_PHONE)
          . '&message=' . urlencode($shortSms);
  $smsResp = @file_get_contents($smsUrl);
  $smsOk = ($smsResp !== false && strpos($smsResp, '<err>0</err>') !== false);
}

if ($emailOk || $smsOk) {
  echo json_encode([
    'ok' => true,
    'email' => $emailOk,
    'sms' => $smsOk,
  ]);
} else {
  http_response_code(500);
  echo json_encode([
    'ok' => false,
    'error' => 'Odeslání selhalo. Zavolejte prosím na +420 731 827 169.'
  ]);
}
